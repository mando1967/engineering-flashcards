# QuizWiz Work Log

---

## October 4, 2025 Session (Part 2) ✅

### Major Refactoring: Multi-Subject & Hierarchical Navigation

**Goal:** Transform QuizWiz from a single-purpose app to support multiple subjects, test sets, and quiz versions with scalable navigation.

### New Architecture

#### Directory Structure
```
tests/
├── Physics/
│   └── PHYS 214 - Test 2/
│       ├── Quiz 2 V1/
│       ├── Quiz 2 V2/
│       ├── Quiz 2 V3/
│       ├── Quiz 2 V4/
│       └── Quiz 2 V5/
└── (future: Math, Chemistry, etc.)
```

#### Configuration System
- **Created `config.json`**: Central configuration file for all subjects, test sets, and quiz versions
- Includes metadata: IDs, names, paths, and image counts
- Easy to extend for new subjects and tests

#### UI Navigation (3-Level Hierarchy)
1. **Subject Tabs** (horizontal): Physics, Math, etc.
2. **Test Sets** (sidebar accordion): PHYS 214 - Test 2, etc.
3. **Quiz Versions** (expandable): V1, V2, V3, etc.
4. **Wizard Mode** per test set: Combines all versions within a test set

### Changes Made ✅

#### File Structure
- **Moved** all Quiz 2 V1-V5 directories to `tests/Physics/PHYS 214 - Test 2/`
- **Created** `config.json` with subject/test set definitions
- All existing flashcards and images preserved in new structure

#### index.html - Complete Refactor
- **Added subject tab navigation** (lines 45-46, 710-728)
- **Updated sidebar** to show test sets with accordion expansion (lines 751-815)
- **Refactored Wizard Mode** to work per test set instead of globally (lines 559-644)
- **New functions:**
  - `loadConfig()`: Loads config.json asynchronously
  - `createSubjectTabs()`: Builds subject navigation tabs
  - `selectSubject()`: Switches between subjects
  - `populateSidebar()`: Dynamically builds test set list
  - `loadWizardMode(testSet)`: Loads all quiz versions for a test set
- **Updated path handling** throughout to use `testSet.path` structure
- **Problem selector** now shows quiz version in parentheses (e.g., "Problem 5 (Quiz 2 V3)")

#### image-mapper.html - Config-Based
- **Added 3-level dropdowns**: Subject → Test Set → Quiz Version (lines 164-172)
- **Integrated config.json** loading and navigation (lines 304-360)
- **Updated path references** to use `currentTestSet.path` structure
- **New functions:**
  - `loadConfig()`: Loads configuration
  - `populateSubjects()`: Fills subject dropdown
  - `updateTestSets()`: Updates test set dropdown based on subject
  - `updateQuizVersions()`: Updates quiz dropdown based on test set
- **Image loading** now uses full hierarchical paths

#### style.css - Subject Tab Styling
- **Added `.subject-tabs`**: Horizontal tab container styling (lines 104-109)
- **Added `.subject-tab`**: Individual tab styling with hover/active states (lines 111-131)
- **Added `.sidebar-content`**: Scrollable content area (lines 133-136)
- Blue theme for active tabs, smooth transitions

### Benefits

✨ **Scalability**: Easy to add new subjects (Math, Chemistry, Biology, etc.)
✨ **Organization**: Clear hierarchy of Subject → Test → Version
✨ **Flexibility**: Each test set can have different number of quiz versions
✨ **Maintainability**: Single config file instead of hardcoded arrays
✨ **User Experience**: Intuitive navigation with visual feedback
✨ **Wizard Mode**: Scoped to test sets, more meaningful practice sessions

### Additional Enhancements (Session 2 Continuation)

**UI Polish:**
- Added wizard-themed tooltips with purple gradient across all interactive elements
- Implemented MedievalSharp font for magical "Quiz Wizard" title
- Updated timer options to 1-10 minutes (granular control)
- Redesigned Wizard Mode button: moved to bottom, lighter accordion-matching color, two-line label
- Increased sidebar height from 75vh to 94vh (25% taller)
- Removed Load Flashcards button - quiz loads automatically on accordion click

**State Persistence:**
- Save `currentIndex` (problem number) to cookies
- Restore position, answers, stats when switching between quizzes
- Auto-save progress on Next, Back, and Jump navigation
- Each quiz maintains completely independent state

**Bug Fixes:**
- Tooltip positioning: wrapper spans for select elements, explicit z-index hierarchy
- Clear Progress tooltip: displays below button with high z-index
- Hide button tooltip: removed (positioning issues with vertical button)
- Accordion behavior: only one quiz open at a time, clear active state
- Image paths: correctly resolved in hierarchical directory structure

**Configuration:**
- Renamed PHYS 214 - Test 1 → PHYS 214 - Test 2
- Updated config.json, directory structure, and WORK_LOG.md

### Testing Status
- All features tested and working
- Tooltips displaying correctly (except hide button - removed)
- State persistence verified across quiz switches
- Accordion navigation smooth and intuitive

### Lessons Learned 📚

**1. CSS Tooltip Positioning with Pseudo-Elements**
- **Issue**: Tooltips using `::after` and `::before` pseudo-elements were being cut off by browser edges or covered by other elements
- **Solution**: 
  - Always explicitly set BOTH `top`/`bottom` and `left`/`right` positions (e.g., `top: calc(100% + 12px)` AND `bottom: auto`)
  - Use proper z-index hierarchy: Set parent containers to lower z-index (1-2) and tooltips to very high z-index (999999)
  - Consider element placement when choosing tooltip direction (above/below/left/right)
  - For buttons at screen edges, position tooltips away from the edge (e.g., right for left-side buttons)
- **Prevention**: Test tooltip positioning at all screen edges during development

**2. Select Elements and Pseudo-Elements**
- **Issue**: `<select>` dropdowns don't support `::after` pseudo-elements for tooltips
- **Solution**: Wrap select elements in a `<span class="tooltip-trigger">` container
- **Prevention**: Always use wrapper elements for form controls when applying pseudo-element styling

**3. Accordion State Management**
- **Issue**: Multiple accordions expanding/collapsing unexpectedly; unclear which quiz is loaded
- **Solution**: 
  - Implement "only one open at a time" logic by closing all siblings before opening new one
  - Remove "Load Flashcards" button; make accordion header trigger both expand AND load
  - Use visual indicators (darker background + border) for active quiz
- **Prevention**: Design accordion behavior explicitly before implementation

**4. Image Path Resolution in Hierarchical Structure**
- **Issue**: Images not loading after directory restructure
- **Solution**: 
  - Update image paths to full paths in `loadFlashcardsFrom()` before rendering
  - Remove redundant path prefixes in rendering code
  - Debug with console logging to verify constructed paths
- **Prevention**: Centralize path construction logic; test image loading immediately after restructure

**5. State Persistence Across Quiz Switches**
- **Issue**: User loses position and progress when switching between quizzes
- **Solution**:
  - Save `currentIndex` (problem number) in cookies along with answers and stats
  - Restore full state when loading a quiz (position, answers, performance)
  - Save progress on every navigation action (next, prev, jump)
- **Prevention**: Design state management comprehensively before implementing navigation features

**6. CSS Specificity and Nested Components**
- **Issue**: Nested quiz accordions inherited parent styles, causing conflicts
- **Solution**: 
  - Use more specific selectors (e.g., `.quiz-accordion > .accordion-content`)
  - Apply `!important` judiciously when necessary to override inherited styles
  - Use child selector `>` instead of descendant selector when targeting direct children
- **Prevention**: Plan CSS hierarchy with nesting in mind; test nested components early

**7. Dynamic Content and Event Listeners**
- **Issue**: Event listeners not firing on dynamically created elements
- **Solution**: 
  - Attach event listeners immediately after creating elements with `appendChild`
  - Use `createElement()` and `addEventListener()` instead of `innerHTML` with inline handlers for complex interactions
  - Verify element structure in browser DevTools
- **Prevention**: Test interactive elements immediately after dynamic creation

**8. Config-Driven Development**
- **Success**: Using `config.json` made path changes trivial (rename directory → update one config line)
- **Best Practice**: 
  - Store all structural data (paths, names, IDs) in centralized config
  - Load config once on startup; reference throughout app
  - Makes scaling and modifications significantly easier
- **Prevention**: Always consider config-driven approach for data-heavy apps

---

## October 4, 2025 Session (Part 1) ✅

### Issue Resolved: Image Mapper Display Bug

**Root Cause Identified:**
- Problem 18 referenced `Quiz 2 V3-5.png` which doesn't exist in the file system
- Only images 0-4 exist (Quiz 2 V3-0.jpg through Quiz 2 V3-4.png)
- The image-mapper correctly parsed the IMAGE tag but `includes()` returned false because the referenced image wasn't in the available images array
- This caused no image to appear as selected in the UI

**Debugging Process:**
- Added comprehensive console logging to image-mapper.html
- Discovered that mappings array contained "Quiz 2 V3-5.png" but available images only had 0-4
- Confirmed file system only has 5 images, not 6

### Changes Made ✅

#### Quiz 2 V3 Flashcards - Problem Numbering Fixed
**Issue:** Problems 16, 17, 18 were incorrect/out of order
- **Problem 16**: Was showing circuit problem with I1, I2, I3 - INCORRECT
- **Problem 17**: Was showing neon lamp problem (not in original quiz) - INCORRECT  
- **Problem 18**: Referenced missing image V3-5.png - INCORRECT

**Fixed:**
- **Problem 16**: Now correctly shows charged conducting sphere (16 points, no image)
- **Problem 17**: Now correctly shows circuit with I1, I2, I3 currents (16 points, IMAGE: V3-3.png)
- **Problem 18**: Now uses existing image V3-4.png instead of missing V3-5.png
- Removed incorrect Problem 17 (neon lamp - not in original Quiz 2 V3)

#### image-mapper.html Updates
- Updated Quiz 2 V3 image count from 6 to 5 (line 308)
- Added enhanced debugging for Problem 18 (lines 214-228, 354-365)
- Debug logs show problem number, index, filenames, and includes() results

#### index.html - Cache-Busting Added
- Added `?t=${Date.now()}` to all flashcards.txt fetch requests (lines 564, 776, 790)
- Prevents browser/server caching issues when flashcard files are updated
- Ensures users always get the latest version

### Final Image Mapping for Quiz 2 V3
- Problem 8: Quiz 2 V3-1.png
- Problems 10-14: Quiz 2 V3-2.png (shared circuit)
- Problem 17: Quiz 2 V3-3.png (circuit with I1, I2, I3)
- Problem 18: Quiz 2 V3-4.png (flashing lamp)
- Problem 16: No image (charged sphere)

### Verification ✅
- Image mapper displays all 18 problems correctly
- All images show proper selections
- index.html displays correct problems and images
- All three browsers confirmed working after cache-busting implementation

---

## October 2, 2025 Session

### Completed Work ✅

#### Quiz 2 V2 Flashcards
- Fixed all formatting errors with TAB delimiters
- Corrected line breaks for all problems
- All 20 problems properly formatted

#### Quiz 2 V3 Flashcards
- Fixed fragmented problems 15-17 that were split incorrectly
- Restored proper line breaks for all problems
- All 18 problems now have correct structure

#### Quiz 2 V5 Flashcards
- Fixed problem 5 - removed wrong answer (was copied from problem 4)
- Changed to "Need image data to determine correct ranking"

#### image-mapper.html Tool
- **Fixed critical bug**: Changed regex from `/\s{2,}/g` to `/ {2,}/g` (line 387)
  - Was removing all whitespace including newlines
  - Now only removes multiple spaces, preserves line breaks
- Enhanced image tag removal (lines 383-387)
- Improved image tag placement to first line only (lines 396-414)
- Enhanced parser to skip fragments without valid problem numbers (line 267)
