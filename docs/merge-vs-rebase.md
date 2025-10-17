# Merge vs Rebase Guide

## The Fundamental Difference

Both `merge` and `rebase` integrate changes from one branch into another, but they do it differently.

### Visual Comparison

**Before Integration:**
```
main:     A---B---C
               \
feature:        D---E
```

**After Merge:**
```
main:     A---B---C-------M
               \         /
feature:        D---E---/
```

**After Rebase:**
```
main:     A---B---C
                   \
feature:            D'---E'
```

## Merge

### What is Merge?

Merge creates a new "merge commit" that combines the histories of two branches.

```bash
git checkout main
git merge feature-branch
```

### How It Works

1. Git finds the common ancestor of both branches
2. Git applies changes from both branches
3. Git creates a new commit with two parents
4. History is preserved exactly as it happened

### Types of Merge

#### 1. Fast-Forward Merge

When there are no new commits on the target branch:

**Before:**
```
main:     A---B
               \
feature:        C---D
```

**After:**
```
main:     A---B---C---D
feature:            C---D
```

```bash
git merge feature-branch
# Result: Fast-forward
```

#### 2. Three-Way Merge

When both branches have new commits:

**Before:**
```
main:     A---B---C
               \
feature:        D---E
```

**After:**
```
main:     A---B---C-------M
               \         /
feature:        D---E---/
```

```bash
git merge feature-branch
# Result: Merge commit created
```

#### 3. No-Fast-Forward Merge

Force a merge commit even when fast-forward is possible:

```bash
git merge --no-ff feature-branch
```

**Before:**
```
main:     A---B
               \
feature:        C---D
```

**After:**
```
main:     A---B-------M
               \     /
feature:        C---D
```

### Pros of Merge

✅ **Preserves complete history**
   - Shows when features were integrated
   - Can see parallel development

✅ **Safe for shared branches**
   - Doesn't rewrite history
   - No force-push needed

✅ **Easy to understand**
   - Straightforward operation
   - Less room for error

✅ **Traceable**
   - Can see exactly when branches merged
   - Easy to revert entire features

### Cons of Merge

❌ **Cluttered history**
   - Many merge commits
   - Harder to follow linear progression

❌ **Complex graph**
   - Difficult to visualize
   - Tool dependent for clarity

❌ **Noise in log**
   - Merge commits may not add value
   - Makes `git log` harder to read

### When to Use Merge

1. **Integrating feature branches into main**
   ```bash
   git checkout main
   git merge feature/new-login
   ```

2. **Updating a long-lived branch**
   ```bash
   git checkout develop
   git merge main
   ```

3. **Working on shared/public branches**
   - Multiple people working on the same branch
   - Already pushed to remote

4. **You want to preserve the context of when features were added**

## Rebase

### What is Rebase?

Rebase moves your branch to start from a different commit, replaying your changes on top.

```bash
git checkout feature-branch
git rebase main
```

### How It Works

1. Git finds the common ancestor
2. Git temporarily saves your commits
3. Git resets your branch to the target
4. Git replays your commits one by one
5. Each commit gets a new SHA (rewritten history)

### Visual Explanation

**Before Rebase:**
```
main:     A---B---C
               \
feature:        D---E
```

**After Rebase:**
```
main:     A---B---C
                   \
feature:            D'---E'
```

Note: D' and E' are new commits (different SHAs) with the same changes as D and E.

### Types of Rebase

#### 1. Standard Rebase

Move your branch to start from the latest main:

```bash
git checkout feature-branch
git rebase main
```

#### 2. Interactive Rebase

Edit, reorder, or squash commits:

```bash
git rebase -i HEAD~3
```

**Interactive Options:**
```
pick abc123 First commit
reword def456 Second commit  # Edit commit message
squash ghi789 Third commit   # Combine with previous
fixup jkl012 Fourth commit   # Combine, discard message
drop mno345 Fifth commit     # Remove this commit
```

#### 3. Rebase onto Different Base

```bash
git rebase --onto new-base old-base feature-branch
```

### Pros of Rebase

✅ **Linear, clean history**
   - Easy to follow
   - Professional looking log
   - Clear progression

✅ **No merge commits**
   - Every commit is meaningful
   - Cleaner `git log`

✅ **Easier to bisect**
   - `git bisect` works better with linear history
   - Easier to find bugs

✅ **Better for small teams**
   - Less overhead
   - Clearer feature development

### Cons of Rebase

❌ **Rewrites history**
   - Changes commit SHAs
   - Dangerous on shared branches
   - Requires force-push

❌ **Loses context**
   - Can't see when features were integrated
   - Parallel development is hidden

❌ **More complex**
   - Steeper learning curve
   - More room for error
   - Can be confusing during conflicts

❌ **Conflicts at each commit**
   - May need to resolve multiple times
   - For same conflict across commits

### When to Use Rebase

1. **Updating your local feature branch**
   ```bash
   git checkout feature/my-work
   git rebase main
   ```

2. **Cleaning up commits before PR**
   ```bash
   git rebase -i HEAD~5
   # Squash, reword, reorder commits
   ```

3. **Maintaining a linear history**
   - For projects that prefer clean history
   - Before merging to main

4. **Private branches only**
   - Never pushed yet
   - Or only you work on it

## The Golden Rule

### ⚠️ NEVER REBASE PUBLIC/SHARED BRANCHES ⚠️

```bash
# ❌ NEVER DO THIS!
git checkout main
git rebase feature-branch

# ❌ NEVER DO THIS!
git checkout shared-team-branch
git rebase main

# ✅ DO THIS INSTEAD
git checkout main
git merge feature-branch
```

**Why?**
- Rewrites history for everyone
- Others' commits become invalid
- Forces everyone to re-clone
- Causes confusion and lost work

## Practical Workflows

### Workflow 1: Feature Development with Rebase

```bash
# Day 1: Start feature
git checkout -b feature/user-profile
# ... make commits ...
git commit -m "feat: add profile component"

# Day 2: Update with latest main
git fetch origin
git rebase origin/main
# ... resolve any conflicts ...

# Day 3: Clean up history
git rebase -i HEAD~5
# Squash, reword commits

# Day 4: Create PR (using merge)
# Open PR: feature/user-profile → main
# After approval: Merge (not rebase) into main
```

### Workflow 2: Feature Development with Merge

```bash
# Day 1: Start feature
git checkout -b feature/user-profile
# ... make commits ...
git commit -m "feat: add profile component"

# Day 2: Update with latest main
git fetch origin
git merge origin/main
# ... resolve any conflicts ...

# Day 3: No cleanup needed
# History shows actual development

# Day 4: Create PR and merge
# Open PR: feature/user-profile → main
# After approval: Merge into main
```

### Workflow 3: Hybrid Approach (Recommended)

```bash
# Use rebase for local cleanup
git checkout feature/user-profile
git rebase -i HEAD~5  # Clean up commits

# Use rebase to update from main
git fetch origin
git rebase origin/main  # Keep linear history

# Use merge to integrate into main
git checkout main
git merge --no-ff feature/user-profile  # Preserve feature context
```

## Conflict Resolution

### Merge Conflicts

```bash
git merge feature-branch
# CONFLICT!

# Resolve in file
git add resolved-file.txt

# One commit to finish
git commit
```

### Rebase Conflicts

```bash
git rebase main
# CONFLICT in commit 1!

# Resolve conflict
git add resolved-file.txt
git rebase --continue

# CONFLICT in commit 2!
# Resolve again
git add resolved-file.txt
git rebase --continue

# May need to repeat for each commit
```

**Tip:** With rebase, you might resolve the same conflict multiple times if it appears in several commits.

## Interactive Rebase Examples

### Example 1: Squash Commits

**Before:**
```
* e4f3b2c (HEAD -> feature) Fix typo in comment
* d3e2a1b Add error handling
* c2d1e0f Fix linting issues
* b1c0d9e Add user registration
```

```bash
git rebase -i HEAD~4
```

**Interactive editor:**
```
pick b1c0d9e Add user registration
fixup c2d1e0f Fix linting issues
fixup d3e2a1b Add error handling
fixup e4f3b2c Fix typo in comment
```

**After:**
```
* a1b2c3d (HEAD -> feature) Add user registration
```

### Example 2: Reword Commit Messages

```bash
git rebase -i HEAD~3
```

**Interactive editor:**
```
pick a1b2c3d Add user registration
reword d4e5f6g Update database schema
pick g7h8i9j Add tests
```

Save and close. Git will prompt you to edit the commit message for the second commit.

### Example 3: Reorder Commits

```bash
git rebase -i HEAD~3
```

**Before:**
```
pick a1b2c3d Add tests
pick d4e5f6g Add feature
pick g7h8i9j Add documentation
```

**After:**
```
pick d4e5f6g Add feature
pick a1b2c3d Add tests
pick g7h8i9j Add documentation
```

### Example 4: Split a Commit

```bash
git rebase -i HEAD~3
```

**Interactive editor:**
```
edit a1b2c3d Big commit to split
pick d4e5f6g Another commit
```

**Then:**
```bash
# Rebase stops at the commit
git reset HEAD^

# Stage and commit pieces separately
git add file1.js
git commit -m "feat: add file1"

git add file2.js
git commit -m "feat: add file2"

# Continue rebase
git rebase --continue
```

## Commands Cheat Sheet

### Merge Commands

```bash
# Basic merge
git merge branch-name

# Merge without fast-forward
git merge --no-ff branch-name

# Merge with custom message
git merge branch-name -m "Custom merge message"

# Abort merge
git merge --abort

# Continue merge after resolving conflicts
git commit  # No special command needed
```

### Rebase Commands

```bash
# Basic rebase
git rebase branch-name

# Interactive rebase
git rebase -i HEAD~3
git rebase -i commit-sha

# Rebase onto different base
git rebase --onto new-base old-base

# Continue rebase after resolving conflicts
git rebase --continue

# Skip current commit
git rebase --skip

# Abort rebase
git rebase --abort

# Preserve merge commits during rebase
git rebase -p branch-name
```

## Common Scenarios

### Scenario 1: Keep Feature Branch Updated

**Using Merge:**
```bash
git checkout feature-branch
git merge main
```

**Using Rebase:**
```bash
git checkout feature-branch
git rebase main
```

### Scenario 2: Combine Multiple Commits

**Using Interactive Rebase:**
```bash
git rebase -i HEAD~3
# Use 'squash' or 'fixup'
```

**Using Reset and Commit:**
```bash
git reset --soft HEAD~3
git commit -m "Combined commit message"
```

### Scenario 3: Fix Commit Message

**Last commit:**
```bash
git commit --amend -m "New message"
```

**Older commit:**
```bash
git rebase -i HEAD~3
# Use 'reword' for the commit
```

## Best Practices

### 1. Choose Based on Context

| Situation | Use |
|-----------|-----|
| Updating local feature branch | Rebase |
| Cleaning up local commits | Interactive rebase |
| Integrating to main | Merge |
| Public/shared branches | Merge |
| Want to preserve history | Merge |
| Want clean history | Rebase |

### 2. Team Agreement

Decide as a team:
- When to use merge vs rebase
- Whether to allow rebasing
- How to handle feature branch updates

### 3. Documentation

Document your team's strategy:
```markdown
# Our Git Strategy

- Feature branches: Rebase locally to clean up
- Updating feature branch: Rebase from main
- Merging to main: Merge with --no-ff
- Never rebase public branches
```

### 4. Protect Main Branch

Set up GitHub branch protection:
- Require pull requests
- Require reviews
- Require status checks
- Restrict force pushes

## Practice Exercises

### Exercise 1: Practice Merge

```bash
# Setup
git init merge-practice
cd merge-practice
echo "Line 1" > file.txt
git add file.txt
git commit -m "Initial commit"

# Create and merge a feature
git checkout -b feature/add-line
echo "Line 2" >> file.txt
git commit -am "Add line 2"

git checkout main
git merge feature/add-line

# Check the history
git log --oneline --graph
```

### Exercise 2: Practice Rebase

```bash
# Setup similar to Exercise 1
git checkout -b feature/add-line-rebase
echo "Line 3" >> file.txt
git commit -am "Add line 3"

git checkout main
echo "Main line" >> file.txt
git commit -am "Add main line"

# Rebase feature onto main
git checkout feature/add-line-rebase
git rebase main

# Check the history
git log --oneline --graph
```

### Exercise 3: Interactive Rebase

```bash
# Create messy history
git checkout -b feature/messy
echo "Change 1" >> file.txt && git commit -am "Change 1"
echo "Change 2" >> file.txt && git commit -am "typo"
echo "Change 3" >> file.txt && git commit -am "Fix typo"
echo "Change 4" >> file.txt && git commit -am "Real change"

# Clean it up
git rebase -i HEAD~4
# Squash the typo commits
```

## Summary

### Quick Decision Guide

**Use Merge when:**
- Working with public/shared branches
- You want to preserve the full history
- Multiple people working on the same branch
- You want to see when features were integrated

**Use Rebase when:**
- Updating your local feature branch
- Cleaning up commits before creating PR
- You want a linear, clean history
- Working on private branches only

### Remember

1. **The Golden Rule**: Never rebase public branches
2. **Merge preserves history**: Shows what actually happened
3. **Rebase rewrites history**: Makes it look cleaner
4. **Both are useful**: Use them for different purposes
5. **Team agreement**: Most important factor

The best approach is often a hybrid: rebase locally for clean history, merge to integrate into main branches.
