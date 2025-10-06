# QuizWiz Development - Lessons Learned

*Last Updated: 2025-10-05*

This document captures important lessons learned during QuizWiz development to avoid repeating mistakes and improve future development efficiency.

---

## 1. JSON & LaTeX Integration

### Issue
LaTeX commands in JSON files were not rendering correctly.

### Solution
- **Double-escape backslashes in JSON**: Use `\\` for LaTeX commands
  - Example: `$\\mathbf{F}_2$`, `$\\approx$`, `$\\theta_x$`
- JSON parser treats `\` as escape character, so `\\` becomes `\` in the actual string

### Best Practice
Always use double backslashes for LaTeX in JSON files. Test rendering immediately after adding LaTeX content.

---

## 2. Markdown Parser Integration with MathJax

### Issue
Adding marked.js for Markdown parsing broke LaTeX rendering and caused undefined errors.

### Solution
1. **Load order matters**: Load marked.js synchronously before MathJax
   ```html
   <script src="marked.min.js"></script>
   <script defer src="mathjax.js"></script>
   ```

2. **Always validate before parsing**:
   ```javascript
   typeof marked !== 'undefined' && marked.parse && content ? marked.parse(content) : (content || '')
   ```

3. **Separate concerns**: Only parse Markdown in explanations, not in short answer fields with LaTeX

### Best Practice
- Check library existence AND method existence before calling
- Never pass `undefined` or `null` to parsing functions
- Provide fallback values with `|| ''`

---

## 3. Array Validation in JavaScript

### Issue
Empty arrays (`[]`) are truthy in JavaScript, causing logic errors.

### Solution
Check for both existence AND length:
```javascript
if (data.choices && data.choices.length > 0) {
  // Process choices
}
```

### Best Practice
For arrays, always check `.length > 0`, not just truthiness.

---

## 4. Quiz Type Detection

### Issue
Code assumed all quizzes were multiple-choice, causing errors for free-response questions.

### Solution
Distinguish between quiz types:
- **Multiple-choice**: `choices.length > 0`
- **Free-response**: `choices.length === 0` or no choices array

Only show selection validation for multiple-choice questions.

### Best Practice
Design code to handle multiple question formats from the start. Don't assume data structure.

---

## 5. URL Encoding for File Paths

### Issue
Paths with spaces (e.g., "CE 333/Test 1") failed to load.

### Solution
```javascript
const encodedPath = path.split('/').map(segment => encodeURIComponent(segment)).join('/');
```

Encode each segment separately, preserving path structure and query strings.

### Best Practice
Always URL-encode user-generated or dynamic path segments, but preserve delimiters and query strings.

---

## 6. Configuration-Driven UI Elements

### Issue
"Wizard Mode" button appeared for single-test subjects where it wasn't useful.

### Solution
Make UI elements conditional based on config:
```javascript
if (testSet.tutorPath) {
  // Show Wizard Mode button
}
```

### Best Practice
Tie UI element visibility to configuration data, not hardcoded logic.

---

## 7. Incremental Testing Strategy

### Issue
Multiple changes made at once made debugging difficult.

### Solution
- Test after each significant change
- Use browser console to catch errors immediately
- Verify with actual production data, not test data

### Best Practice
Make small, testable changes. Verify each change works before moving to the next.

---

## 8. Plain Text vs Rendered Content

### Issue
Answers displayed as plain text instead of rendered LaTeX/Markdown.

### Solution
- Use LaTeX syntax (`$...$`) for math in answer fields
- Use Markdown syntax (`##`) for structure in explanations
- Ensure MathJax processes entire card after rendering

### Best Practice
Separate formatting concerns: LaTeX for math, Markdown for structure, HTML for layout.

---

## General Development Principles

1. **Validate all inputs** - Check for existence, type, and content before processing
2. **Fail gracefully** - Provide fallbacks for missing libraries or data
3. **Test with real data** - Don't assume data structure; test with actual production data
4. **Load order matters** - Dependencies must load before code that uses them
5. **Escape appropriately** - Different contexts (JSON, HTML, URLs) require different escaping
6. **Check the console** - Browser console errors provide exact line numbers and error types
7. **Empty != Missing** - Empty arrays/strings exist but are "empty"; check both existence and content

---

## Quick Reference: Common Patterns

### Safe Markdown Parsing
```javascript
const parsed = (typeof marked !== 'undefined' && marked.parse && content) 
  ? marked.parse(content) 
  : (content || '');
```

### Safe Array Processing
```javascript
if (array && array.length > 0) {
  array.forEach(item => { /* process */ });
}
```

### LaTeX in JSON
```json
{
  "answer": "$\\\\mathbf{F}_2 \\\\approx 66$ lb"
}
```

### URL Encoding Paths
```javascript
const encoded = path.split('/').map(encodeURIComponent).join('/');
```

---

*This document should be updated whenever significant lessons are learned during development.*
