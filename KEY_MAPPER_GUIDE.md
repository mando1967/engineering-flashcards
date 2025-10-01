# Quiz Key Reference Mapper Guide

## Overview
The **key-mapper.html** tool allows you to easily mark problems that should reference the quiz key PDF instead of showing the answer inline in the flashcard app.

## How to Use

### Step 1: Open the Tool
Open `key-mapper.html` in your browser (e.g., `http://localhost/quizwiz/key-mapper.html`)

### Step 2: Select a Quiz Set
1. Choose a quiz from the dropdown (Quiz 2 V1, V2, V3, V4, or V5)
2. Click "Load Quiz"

### Step 3: Mark Problems for Quiz Key Reference
- Each problem is displayed with its question text
- Click the **"🔑 Refer to Quiz Key"** button for any problem where you want to hide the inline answer
- When selected, the button changes to **"🔑✓ Referring to Quiz Key"** and the problem is highlighted in yellow
- Click again to deselect if needed

### Step 4: Export Updated Flashcards
1. Click **"Export Updated Flashcards"** button
2. The updated flashcards.txt content will appear below
3. Click **"📋 Copy to Clipboard"** to copy the content
4. Paste it into your `tests/[Quiz Name]/flashcards.txt` file

## What Happens?

When you mark a problem to refer to the quiz key:

1. **In the mapper**: The answer section is replaced with:
   ```
   Answer: [SEE_KEY] Please refer to the Quiz Key PDF for the detailed solution.
   ```

2. **In the flashcard app**: When students reveal the answer, they will see:
   - A prominent yellow/orange box with a key icon 🔑
   - A message: "Please refer to the Quiz Key for the detailed solution."
   - A link to open the Quiz Key PDF directly
   - The inline answer and explanation are hidden

## Benefits

- **Simplifies complex problems**: For problems with lengthy visual solutions, students can view the formatted PDF
- **Reduces duplication**: Avoid typing out complex step-by-step solutions that already exist in the key
- **Maintains engagement**: Students still attempt the problem before being directed to the key
- **Easy management**: Visual interface makes it simple to see which problems reference the key

## Example Use Cases

Best for:
- Problems with extensive diagrams or graphs in the solution
- Multi-step derivations that are clearer in the formatted key
- Problems where the solution requires significant mathematical notation
- Any problem where the PDF key provides a better learning experience

## Tips

- The tool preserves your existing image mappings (`[IMAGE:...]` tags)
- You can still use both image references AND quiz key references on the same problem
- The statistics bar shows how many problems are set to refer to the key
- Problems marked with quiz key reference won't show inline explanations or resource links

## Technical Details

The tool adds a `[SEE_KEY]` tag to the answer field, which the main app detects and renders as a special quiz key reference box with a direct link to the answer key PDF.
