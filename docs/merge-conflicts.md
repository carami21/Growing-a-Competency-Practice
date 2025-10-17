# Merge Conflicts Guide

## What is a Merge Conflict?

A merge conflict occurs when Git cannot automatically merge changes from different branches because the same part of a file was modified in different ways.

## Why Conflicts Happen

Conflicts occur when:
1. Two people edit the same lines in a file
2. One person deletes a file while another edits it
3. One person renames a file while another edits the old location
4. Complex changes overlap in unexpected ways

## Understanding Conflict Markers

When a conflict occurs, Git marks the conflicting sections in your files:

```
<<<<<<< HEAD
This is the content from your current branch
=======
This is the content from the branch being merged
>>>>>>> feature-branch
```

**Breakdown:**
- `<<<<<<< HEAD`: Start of your changes (current branch)
- `=======`: Separator between the two versions
- `>>>>>>> branch-name`: End of the incoming changes

## Practice Scenarios

### Scenario 1: Simple Line Conflict

**Setup:**
```bash
# Create a file on main
git checkout -b main
echo "Hello World" > greeting.txt
git add greeting.txt
git commit -m "Add greeting"

# Create branch A
git checkout -b feature/greeting-formal
echo "Good Morning" > greeting.txt
git commit -am "Make greeting formal"

# Go back and create branch B
git checkout main
git checkout -b feature/greeting-casual
echo "Hey there" > greeting.txt
git commit -am "Make greeting casual"

# Try to merge - CONFLICT!
git checkout main
git merge feature/greeting-formal  # This works
git merge feature/greeting-casual  # This conflicts!
```

**Result:**
```
Auto-merging greeting.txt
CONFLICT (content): Merge conflict in greeting.txt
Automatic merge failed; fix conflicts and then commit the result.
```

**Resolution:**
```bash
# Open greeting.txt
# You'll see:
<<<<<<< HEAD
Good Morning
=======
Hey there
>>>>>>> feature/greeting-casual

# Choose which version to keep or combine them
# Option 1: Keep formal
Good Morning

# Option 2: Keep casual
Hey there

# Option 3: Combine both
Good Morning! Hey there!

# After resolving, mark as resolved
git add greeting.txt
git commit -m "Merge feature/greeting-casual into main"
```

### Scenario 2: Multiple File Conflicts

Create a conflict across multiple files:

**Setup:**
```bash
# File structure
project/
  ├── config.json
  ├── README.md
  └── src/
      └── app.js

# Branch A changes all three files
# Branch B also changes all three files differently
```

**Resolution Strategy:**
1. Handle one file at a time
2. Use `git status` to track progress
3. Test after each resolution

```bash
# Check which files are conflicted
git status

# Resolve each file
# After resolving all files
git add .
git commit
```

### Scenario 3: Delete vs Modify Conflict

**Setup:**
```bash
# Branch A: Delete file
git checkout -b feature/remove-old-code
git rm deprecated.js
git commit -m "Remove deprecated code"

# Branch B: Modify the same file
git checkout main
git checkout -b feature/update-deprecated
echo "// Updated" >> deprecated.js
git commit -am "Update deprecated code"

# Merge - CONFLICT!
git checkout main
git merge feature/remove-old-code    # Works
git merge feature/update-deprecated   # Conflict!
```

**Resolution:**
```bash
# Git will show:
CONFLICT (modify/delete): deprecated.js deleted in HEAD 
and modified in feature/update-deprecated.

# Decision time:
# Keep the deletion (accept removal)
git rm deprecated.js

# OR keep the modification (restore file)
git add deprecated.js

# Then commit
git commit
```

## Resolution Strategies

### Strategy 1: Manual Resolution

Edit the file directly:

```bash
# 1. Open the conflicted file
vim greeting.txt

# 2. Look for conflict markers
<<<<<<< HEAD
Current content
=======
Incoming content
>>>>>>> feature-branch

# 3. Edit to your desired state
Final content combining both or choosing one

# 4. Remove conflict markers
# 5. Save the file

# 6. Mark as resolved
git add greeting.txt

# 7. Complete the merge
git commit
```

### Strategy 2: Accept Theirs or Ours

When you know which version to keep:

```bash
# Accept the incoming changes (theirs)
git checkout --theirs filename.txt
git add filename.txt

# Accept your current changes (ours)
git checkout --ours filename.txt
git add filename.txt

# Then commit
git commit
```

### Strategy 3: Use a Merge Tool

Visual merge tools make conflicts easier to resolve:

```bash
# Configure merge tool (one-time setup)
git config --global merge.tool vimdiff
# Or use: meld, kdiff3, p4merge, etc.

# Launch merge tool
git mergetool

# After resolving in the tool
git commit
```

**Popular Merge Tools:**
- **VS Code**: Built-in merge conflict resolver
- **Meld**: Visual diff and merge tool
- **KDiff3**: Cross-platform diff tool
- **P4Merge**: Perforce visual merge tool
- **Beyond Compare**: Commercial option

### Strategy 4: Abort and Retry

If things get messy, start over:

```bash
# Abort the merge
git merge --abort

# Or abort a rebase
git rebase --abort

# Clean up and try again
git status  # Make sure you're clean
# Try merge again with a different strategy
```

## Common Conflict Patterns

### Pattern 1: Import Statements

**Conflict:**
```javascript
<<<<<<< HEAD
import { ComponentA, ComponentB } from './components';
import { helperA } from './utils';
=======
import { ComponentA, ComponentC } from './components';
import { helperB } from './utils';
>>>>>>> feature-branch
```

**Resolution:**
```javascript
// Combine all imports
import { ComponentA, ComponentB, ComponentC } from './components';
import { helperA, helperB } from './utils';
```

### Pattern 2: Configuration Files

**Conflict:**
```json
<<<<<<< HEAD
{
  "port": 3000,
  "database": "mongodb://localhost/prod"
}
=======
{
  "port": 8080,
  "database": "mongodb://localhost/dev",
  "debug": true
}
>>>>>>> feature-branch
```

**Resolution:**
```json
{
  "port": 8080,
  "database": "mongodb://localhost/prod",
  "debug": true
}
```

### Pattern 3: Package Dependencies

**Conflict:**
```json
<<<<<<< HEAD
"dependencies": {
  "express": "^4.17.1",
  "mongodb": "^4.0.0"
}
=======
"dependencies": {
  "express": "^4.18.0",
  "mongoose": "^6.0.0"
}
>>>>>>> feature-branch
```

**Resolution:**
```json
"dependencies": {
  "express": "^4.18.0",
  "mongodb": "^4.0.0",
  "mongoose": "^6.0.0"
}
```

## Preventing Conflicts

### 1. Communicate with Your Team

- Discuss who's working on what
- Avoid working on the same files simultaneously
- Coordinate big refactorings

### 2. Keep Branches Short-Lived

```bash
# Instead of:
feature/big-rewrite (30 days old, 100 files changed)

# Do this:
feature/refactor-auth (2 days old, 10 files changed)
feature/refactor-api (2 days old, 8 files changed)
feature/refactor-ui (2 days old, 12 files changed)
```

### 3. Pull/Rebase Frequently

```bash
# Update your branch daily
git checkout feature/my-feature
git fetch origin
git rebase origin/main

# Or merge
git merge origin/main
```

### 4. Use Feature Flags

Deploy incomplete features behind flags:

```javascript
// Instead of long-lived branch
if (featureFlags.newCheckout) {
  return <NewCheckoutFlow />;
}
return <OldCheckoutFlow />;
```

### 5. Modularize Your Code

Smaller, focused files = fewer conflicts:

```
// Instead of:
app.js (1000 lines)

// Do this:
src/
  ├── auth/
  │   ├── login.js
  │   └── logout.js
  ├── users/
  │   ├── create.js
  │   └── update.js
  └── products/
      ├── list.js
      └── detail.js
```

## Advanced Conflict Resolution

### Using Three-Way Merge

See all three versions:

```bash
# Show base version (common ancestor)
git show :1:filename.txt

# Show ours (current branch)
git show :2:filename.txt

# Show theirs (incoming branch)
git show :3:filename.txt
```

### Rerere (Reuse Recorded Resolution)

Git can remember how you resolved conflicts:

```bash
# Enable rerere
git config --global rerere.enabled true

# Now when you resolve a conflict, Git remembers
# If the same conflict appears again, Git auto-resolves it
```

### Cherry-Pick Conflicts

When cherry-picking commits:

```bash
# Cherry-pick a commit
git cherry-pick abc123

# If conflict occurs
# Resolve the conflict
git add resolved-file.txt

# Continue cherry-pick
git cherry-pick --continue

# Or abort
git cherry-pick --abort
```

### Rebase Conflicts

During interactive rebase:

```bash
# Start rebase
git rebase -i HEAD~3

# If conflict occurs at a step
# Resolve the conflict
git add resolved-file.txt

# Continue rebase
git rebase --continue

# Or abort
git rebase --abort

# Or skip this commit
git rebase --skip
```

## Conflict Resolution Workflow

### Step-by-Step Process

```bash
# 1. Start the merge/rebase
git merge feature-branch
# Or
git rebase main

# 2. Conflict detected!
# CONFLICT (content): Merge conflict in file.txt
# Automatic merge failed; fix conflicts and then commit the result.

# 3. Check status
git status
# Shows:
# both modified:   file.txt

# 4. Open and resolve the file
# Remove conflict markers
# Choose or combine changes

# 5. Test your resolution
npm test  # Make sure nothing breaks

# 6. Stage the resolved file
git add file.txt

# 7. Continue the operation
git commit  # For merge
# Or
git rebase --continue  # For rebase

# 8. Push your changes
git push origin branch-name
```

## Practice Exercises

### Exercise 1: Create and Resolve a Simple Conflict

```bash
# 1. Initialize a test repo
mkdir conflict-practice
cd conflict-practice
git init

# 2. Create a file on main
echo "Line 1" > test.txt
git add test.txt
git commit -m "Initial commit"

# 3. Create branch A and make changes
git checkout -b branch-a
echo "Line 2 from branch A" >> test.txt
git commit -am "Add line from branch A"

# 4. Go back and create branch B
git checkout main
git checkout -b branch-b
echo "Line 2 from branch B" >> test.txt
git commit -am "Add line from branch B"

# 5. Merge and resolve
git checkout main
git merge branch-a  # Works fine
git merge branch-b  # CONFLICT!

# 6. Open test.txt and resolve
# 7. Complete the merge
git add test.txt
git commit -m "Resolve conflict between branch-a and branch-b"
```

### Exercise 2: Resolve Multi-File Conflict

```bash
# Create conflicts in multiple files
# Practice resolving them one by one
# Use git status to track progress
```

### Exercise 3: Use a Merge Tool

```bash
# Install and configure a merge tool
git config --global merge.tool meld

# Create a conflict
# Resolve using the tool
git mergetool
```

## Troubleshooting

### "I'm Lost in a Merge"

```bash
# Check what's going on
git status

# See the full diff
git diff

# If you want to start over
git merge --abort
```

### "I Resolved but Git Still Shows Conflict"

```bash
# Did you remove all conflict markers?
grep -r "<<<<<<" .
grep -r "======" .
grep -r ">>>>>>" .

# Did you stage the files?
git add resolved-file.txt
```

### "I Accidentally Deleted Important Changes"

```bash
# If you haven't committed yet
git checkout --merge filename.txt

# If you committed, use reflog
git reflog
git reset --hard HEAD@{1}
```

## Best Practices

1. **Resolve conflicts locally before pushing**
   - Don't push conflict markers
   - Test your resolution

2. **Communicate with the team**
   - Let them know you're resolving conflicts
   - Ask for help if needed

3. **Test after resolving**
   - Run tests
   - Manually verify functionality

4. **Keep commits atomic**
   - Makes conflicts easier to resolve
   - Easier to understand what changed

5. **Use descriptive conflict resolution commits**
   ```bash
   # Instead of:
   git commit -m "fixed conflict"
   
   # Do this:
   git commit -m "Merge branch 'feature/auth': resolve conflict in login.js
   
   Kept the new validation logic from feature/auth while
   preserving the error handling from main."
   ```

## Summary

- Conflicts are normal in collaborative development
- Understand conflict markers: `<<<<<<<`, `=======`, `>>>>>>>`
- Use appropriate resolution strategy for each situation
- Test after resolving conflicts
- Prevent conflicts by communicating and merging frequently
- Don't be afraid to ask for help!

Remember: Merge conflicts are an opportunity to understand the codebase better and collaborate with your team!
