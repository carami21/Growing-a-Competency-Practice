# Perfect Commits Guide

## What Makes a Perfect Commit?

A perfect commit is:
1. **Atomic**: Contains one logical change
2. **Complete**: Includes all related changes (code, tests, docs)
3. **Well-described**: Has a clear, informative commit message
4. **Tested**: Passes all tests
5. **Reviewable**: Easy to understand and review

## The Anatomy of a Good Commit Message

### Structure

```
<type>(<scope>): <subject>

<body>

<footer>
```

### Examples

#### Good Commit Messages

```
feat(auth): add user login with JWT authentication

Implement JWT-based authentication system:
- Add login endpoint at /api/auth/login
- Generate JWT tokens with 24h expiration
- Add middleware for token validation
- Include refresh token mechanism

Closes #123
```

```
fix(api): resolve race condition in user creation

The user creation endpoint occasionally created duplicate users
when requests came in simultaneously. Added database-level
unique constraint and proper error handling.

Fixes #456
```

```
docs(readme): update installation instructions

Add missing prerequisites and troubleshooting section
for Windows users experiencing npm installation issues.
```

#### Poor Commit Messages (Avoid These!)

❌ `fixed stuff`
❌ `WIP`
❌ `updated files`
❌ `changes`
❌ `asdf`
❌ `minor updates`

## Practice Exercises

### Exercise 1: Atomic Commits

Create a series of atomic commits for the following scenario:

1. Add a new feature file `calculator.js` with basic operations
2. Add tests for the calculator
3. Update README to document the calculator
4. Fix a bug in the addition function

Each step should be a separate commit!

### Exercise 2: Commit Message Practice

Rewrite these poor commit messages into good ones:

1. `fixed bug` → ?
2. `updates` → ?
3. `added stuff for login` → ?

### Exercise 3: Amending Commits

Practice fixing your last commit:

```bash
# Made a commit but forgot to add a file
git add forgotten-file.js
git commit --amend --no-edit

# Made a commit but want to improve the message
git commit --amend -m "Better commit message"
```

### Exercise 4: Interactive Rebase

Clean up commit history before pushing:

```bash
# Review last 3 commits
git rebase -i HEAD~3

# Options:
# pick = use commit
# reword = use commit, but edit message
# squash = combine with previous commit
# fixup = like squash, but discard message
# drop = remove commit
```

## Commit Types Reference

| Type | Description | Example |
|------|-------------|---------|
| `feat` | New feature | `feat(api): add user registration endpoint` |
| `fix` | Bug fix | `fix(auth): prevent duplicate login sessions` |
| `docs` | Documentation | `docs(api): add endpoint documentation` |
| `style` | Formatting | `style(core): fix indentation in main.js` |
| `refactor` | Code restructuring | `refactor(db): simplify query builder logic` |
| `test` | Adding tests | `test(auth): add integration tests for login` |
| `chore` | Maintenance | `chore(deps): update dependencies to latest` |
| `perf` | Performance | `perf(api): optimize database queries` |
| `ci` | CI/CD changes | `ci(github): add automated testing workflow` |

## Best Practices Checklist

Before committing, ask yourself:

- [ ] Does this commit have a single, clear purpose?
- [ ] Would this commit make sense on its own?
- [ ] Is my commit message descriptive enough?
- [ ] Did I include the "why" in the commit body?
- [ ] Did I reference related issues?
- [ ] Do all tests pass?
- [ ] Did I review my changes with `git diff --cached`?

## Tools to Help

### Git Hooks

Use pre-commit hooks to enforce standards:

```bash
# .git/hooks/commit-msg
#!/bin/sh
commit_msg=$(cat "$1")

# Check commit message format
if ! echo "$commit_msg" | grep -qE "^(feat|fix|docs|style|refactor|test|chore)\(.+\): .+"; then
    echo "Error: Commit message doesn't follow format"
    echo "Format: type(scope): subject"
    exit 1
fi
```

### Commitizen

Install commitizen for interactive commit messages:

```bash
npm install -g commitizen
commitizen init cz-conventional-changelog --save-dev --save-exact
```

Then use `git cz` instead of `git commit`.

## Real-World Example

Let's say you're adding a search feature:

```bash
# 1. Create feature branch
git checkout -b feature/add-search

# 2. Add search function
# ... make changes ...
git add src/search.js
git commit -m "feat(search): add full-text search function

Implement search functionality using fuzzy matching algorithm:
- Support searching across title, content, and tags
- Add search result ranking by relevance
- Include pagination for results (20 per page)

Part of #789"

# 3. Add tests
# ... write tests ...
git add tests/search.test.js
git commit -m "test(search): add unit tests for search function

Add comprehensive test coverage:
- Test fuzzy matching accuracy
- Test pagination
- Test edge cases (empty query, special characters)

Coverage: 95%
Part of #789"

# 4. Update documentation
# ... update docs ...
git add docs/api.md
git commit -m "docs(api): document search endpoint

Add API documentation for new /api/search endpoint:
- Request/response examples
- Query parameters
- Error codes

Part of #789"
```

## Common Mistakes to Avoid

### 1. The "Kitchen Sink" Commit

❌ Committing unrelated changes together:
```bash
git add .
git commit -m "added login, fixed typos, updated deps"
```

✅ Separate into atomic commits:
```bash
git add src/auth.js tests/auth.test.js
git commit -m "feat(auth): add login functionality"

git add README.md docs/guide.md
git commit -m "docs: fix typos in documentation"

git add package.json package-lock.json
git commit -m "chore(deps): update dependencies"
```

### 2. Committing Broken Code

❌ Committing code that doesn't compile or pass tests

✅ Always verify before committing:
```bash
npm test && git commit
```

### 3. Vague Commit Messages

❌ `git commit -m "fix"`

✅ `git commit -m "fix(api): handle null user in profile endpoint"`

## Advanced: Signing Commits

For added security, sign your commits:

```bash
# Generate GPG key
gpg --gen-key

# List keys
gpg --list-secret-keys --keyid-format LONG

# Configure git to use key
git config --global user.signingkey YOUR_KEY_ID
git config --global commit.gpgsign true

# Sign a commit
git commit -S -m "feat(auth): add 2FA support"
```

## Summary

Perfect commits make your project history:
- Easier to understand
- Easier to review
- Easier to debug (with `git bisect`)
- Easier to cherry-pick or revert

Take the time to craft good commits - your future self (and team) will thank you!
