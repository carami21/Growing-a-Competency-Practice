# Branching Strategy Guide

## Why Branching Matters

Branching allows you to:
- Work on features in isolation
- Experiment without breaking main code
- Collaborate with multiple developers
- Maintain different versions simultaneously

## Common Branching Strategies

### 1. GitHub Flow (Recommended for Most Projects)

**Simple and effective for continuous deployment.**

```
main (always deployable)
  ↓
feature/add-login ──→ PR ──→ merge to main
feature/fix-bug ────→ PR ──→ merge to main
```

**Workflow:**
1. Branch off from `main`
2. Add commits
3. Open a Pull Request
4. Review and discuss
5. Deploy and test
6. Merge to `main`

**Pros:**
- Simple to understand
- Works well with CI/CD
- Main branch always deployable

**Cons:**
- Less suitable for scheduled releases
- No clear release management

### 2. Git Flow

**More complex, good for scheduled releases.**

```
main (production)
  ↓
release/v1.2.0
  ↓
develop (integration)
  ↓
feature/add-login
feature/new-dashboard
hotfix/fix-critical-bug
```

**Branch Types:**

| Branch | Purpose | Base | Merge to |
|--------|---------|------|----------|
| `main` | Production code | - | - |
| `develop` | Integration | `main` | `main` (via release) |
| `feature/*` | New features | `develop` | `develop` |
| `release/*` | Release prep | `develop` | `main` and `develop` |
| `hotfix/*` | Emergency fixes | `main` | `main` and `develop` |

**Workflow:**

```bash
# Start new feature
git checkout develop
git checkout -b feature/user-profile

# ... make changes ...
git add .
git commit -m "feat(profile): add user profile page"
git push origin feature/user-profile

# Create PR to merge into develop
# After review, merge to develop

# When ready to release
git checkout develop
git checkout -b release/v1.2.0

# ... final testing, version bumps ...
git commit -m "chore(release): prepare v1.2.0"

# Merge to main
git checkout main
git merge release/v1.2.0
git tag -a v1.2.0 -m "Version 1.2.0"

# Also merge back to develop
git checkout develop
git merge release/v1.2.0
```

**Pros:**
- Clear release management
- Parallel development tracks
- Emergency hotfixes don't disrupt development

**Cons:**
- More complex
- Can be overkill for simple projects

### 3. Trunk-Based Development

**Single main branch with very short-lived feature branches.**

```
main
  ↓
feature/quick-fix (< 1 day) ──→ merge
feature/small-feature (< 2 days) ──→ merge
```

**Pros:**
- Simplest model
- Encourages small, frequent commits
- Minimal merge conflicts

**Cons:**
- Requires feature flags for incomplete features
- Needs strong CI/CD
- Can be risky without good testing

## Branch Naming Conventions

### Format

```
<type>/<short-description>
```

### Types

- `feature/` - New features
- `bugfix/` or `fix/` - Bug fixes
- `hotfix/` - Urgent production fixes
- `release/` - Release preparation
- `docs/` - Documentation changes
- `refactor/` - Code refactoring
- `test/` - Adding tests
- `chore/` - Maintenance tasks

### Examples

✅ **Good Names:**
```
feature/add-user-authentication
feature/implement-payment-gateway
bugfix/fix-login-error
hotfix/patch-security-vulnerability
release/v1.2.0
docs/update-api-documentation
refactor/optimize-database-queries
test/add-integration-tests
```

❌ **Bad Names:**
```
my-branch
test
fix
updates
branch1
temp
```

## Basic Git Branch Commands

### Creating Branches

```bash
# Create new branch
git branch feature/new-feature

# Create and switch to new branch
git checkout -b feature/new-feature

# Create branch from specific commit
git checkout -b hotfix/bug-fix abc123

# Create branch from remote branch
git checkout -b feature/new-feature origin/develop
```

### Switching Branches

```bash
# Switch to existing branch
git checkout feature/new-feature

# Modern alternative (Git 2.23+)
git switch feature/new-feature

# Switch to previous branch
git checkout -
```

### Viewing Branches

```bash
# List local branches
git branch

# List all branches (local and remote)
git branch -a

# List with last commit
git branch -v

# List merged branches
git branch --merged

# List unmerged branches
git branch --no-merged
```

### Deleting Branches

```bash
# Delete merged branch (safe)
git branch -d feature/completed-feature

# Force delete (even if not merged)
git branch -D feature/abandoned-feature

# Delete remote branch
git push origin --delete feature/old-feature
```

## Practice Exercises

### Exercise 1: Basic Branching

Practice creating and switching branches:

```bash
# 1. Create a new feature branch
git checkout -b feature/add-calculator

# 2. Make some changes
echo "console.log('Calculator')" > calculator.js
git add calculator.js
git commit -m "feat(calc): add calculator file"

# 3. Switch back to main
git checkout main

# 4. Create another branch
git checkout -b feature/add-readme

# 5. Make changes
echo "# Calculator" > CALC_README.md
git add CALC_README.md
git commit -m "docs: add calculator readme"

# 6. View all branches
git branch -a
```

### Exercise 2: Feature Development Workflow

Practice a complete feature workflow:

```bash
# 1. Start from main
git checkout main
git pull origin main

# 2. Create feature branch
git checkout -b feature/user-login

# 3. Make multiple commits
# ... develop feature ...
git add src/auth.js
git commit -m "feat(auth): add login function"

git add tests/auth.test.js
git commit -m "test(auth): add login tests"

git add docs/auth.md
git commit -m "docs(auth): document login API"

# 4. Push to remote
git push origin feature/user-login

# 5. Create Pull Request on GitHub

# 6. After review and approval, merge and cleanup
git checkout main
git pull origin main
git branch -d feature/user-login
```

### Exercise 3: Parallel Features

Practice working on multiple features simultaneously:

```bash
# Feature A
git checkout -b feature/add-search
# ... make changes ...
git commit -m "feat(search): implement search"
git push origin feature/add-search

# Switch to Feature B
git checkout main
git checkout -b feature/add-filters
# ... make changes ...
git commit -m "feat(filter): add result filters"
git push origin feature/add-filters

# Switch back to Feature A
git checkout feature/add-search
# ... continue work ...
```

## Advanced Branch Operations

### Cherry-picking Commits

Apply specific commits from one branch to another:

```bash
# Switch to target branch
git checkout main

# Cherry-pick specific commit
git cherry-pick abc123

# Cherry-pick range of commits
git cherry-pick abc123..def456
```

### Stashing Changes

Save uncommitted changes when switching branches:

```bash
# Stash current changes
git stash

# Switch branches
git checkout other-branch

# Come back and apply stash
git checkout original-branch
git stash pop

# List stashes
git stash list

# Apply specific stash
git stash apply stash@{0}
```

### Comparing Branches

```bash
# See commits in feature branch not in main
git log main..feature/new-feature

# See file differences between branches
git diff main..feature/new-feature

# See which files changed
git diff --name-only main..feature/new-feature
```

## Branch Protection Rules

Set up protection on GitHub for important branches:

**Settings → Branches → Branch protection rules**

Recommended rules for `main`:
- ✅ Require pull request reviews before merging
- ✅ Require status checks to pass
- ✅ Require branches to be up to date
- ✅ Include administrators
- ✅ Restrict who can push

## Best Practices

### 1. Keep Branches Short-Lived

- Aim for branches to live < 2-3 days
- Merge frequently to avoid conflicts
- Delete branches after merging

### 2. Update Feature Branches Regularly

```bash
# Stay in sync with main
git checkout feature/my-feature
git fetch origin
git merge origin/main

# Or use rebase (for cleaner history)
git rebase origin/main
```

### 3. One Feature Per Branch

Don't mix unrelated changes in a single branch.

❌ Bad:
```
feature/add-login-and-fix-typos-and-update-deps
```

✅ Good:
```
feature/add-login
docs/fix-typos
chore/update-dependencies
```

### 4. Clean Up Old Branches

```bash
# Delete local branches already merged
git branch --merged | grep -v "\*" | grep -v "main" | xargs -n 1 git branch -d

# Prune remote-tracking branches
git fetch --prune
```

## Visualizing Branches

### Command Line

```bash
# Simple graph
git log --oneline --graph --all

# Detailed graph
git log --graph --all --decorate --oneline

# Create alias for easier use
git config --global alias.tree "log --graph --all --decorate --oneline"
git tree
```

### GUI Tools

- **GitHub Desktop**: Visual branch management
- **GitKraken**: Advanced visualization
- **SourceTree**: Free Atlassian tool
- **Git Graph (VS Code)**: Extension for VS Code

## Common Scenarios

### Scenario 1: Switching Branches with Uncommitted Changes

**Problem:** You have uncommitted changes but need to switch branches.

**Solutions:**

```bash
# Option 1: Commit changes
git add .
git commit -m "WIP: partial work"

# Option 2: Stash changes
git stash
git checkout other-branch
# ... do work ...
git checkout original-branch
git stash pop

# Option 3: Create new branch with changes
git checkout -b feature/save-my-work
git add .
git commit -m "feat: save work in progress"
```

### Scenario 2: Accidentally Committed to Wrong Branch

**Problem:** You made commits on `main` instead of a feature branch.

**Solution:**

```bash
# Create new branch with these commits
git branch feature/my-feature

# Reset main to origin
git fetch origin
git reset --hard origin/main

# Switch to feature branch (commits are there)
git checkout feature/my-feature
```

### Scenario 3: Need to Update Feature Branch

**Problem:** Your feature branch is behind `main`.

**Solution:**

```bash
git checkout feature/my-feature

# Option 1: Merge main into feature
git merge main

# Option 2: Rebase feature on main (cleaner history)
git rebase main
```

## Workflow Comparison

| Aspect | GitHub Flow | Git Flow | Trunk-Based |
|--------|-------------|----------|-------------|
| Complexity | Low | High | Very Low |
| Branch Types | 1-2 | 5 | 1 |
| Release Cycle | Continuous | Scheduled | Continuous |
| Team Size | Any | Large | Small-Medium |
| Learning Curve | Easy | Steep | Easy |
| Best For | Web apps, SaaS | Enterprise, scheduled releases | Fast-moving teams |

## Summary

- Choose a branching strategy that fits your team and project
- Use descriptive branch names
- Keep branches short-lived
- Protect important branches
- Delete merged branches
- Stay in sync with main branch

Remember: The best branching strategy is the one your team actually follows!
