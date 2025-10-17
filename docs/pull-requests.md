# Pull Request Review Guide

## What is a Pull Request?

A Pull Request (PR) is a proposal to merge code changes from one branch into another. It's a collaborative review process that helps maintain code quality.

## Why Code Reviews Matter

- **Catch bugs** before they reach production
- **Share knowledge** across the team
- **Maintain consistency** in code style and architecture
- **Improve code quality** through collective wisdom
- **Onboard new developers** by exposing them to the codebase

## Creating a Good Pull Request

### 1. Before Creating the PR

✅ **Checklist:**
- [ ] Code compiles/runs without errors
- [ ] All tests pass
- [ ] New tests added for new features
- [ ] Code follows style guidelines
- [ ] No debugging code or console.logs
- [ ] Documentation updated
- [ ] Branch is up to date with base branch

### 2. Writing the PR Description

#### PR Title

Use the same format as commit messages:

```
<type>(<scope>): <brief description>
```

Examples:
- `feat(auth): add OAuth2 authentication`
- `fix(api): resolve race condition in user creation`
- `docs(readme): update installation instructions`

#### PR Description Template

```markdown
## Description
Brief summary of what this PR does and why.

## Changes Made
- Bullet point list of specific changes
- Another change
- Yet another change

## Type of Change
- [ ] Bug fix (non-breaking change which fixes an issue)
- [ ] New feature (non-breaking change which adds functionality)
- [ ] Breaking change (fix or feature that would cause existing functionality to not work as expected)
- [ ] Documentation update
- [ ] Refactoring
- [ ] Performance improvement

## Related Issues
Fixes #123
Relates to #456

## Testing
Describe how you tested these changes:
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing performed

### Test Results
Paste test results or screenshots here.

## Screenshots (if applicable)
Before: [screenshot]
After: [screenshot]

## Checklist
- [ ] My code follows the project's style guidelines
- [ ] I have performed a self-review of my code
- [ ] I have commented my code, particularly in hard-to-understand areas
- [ ] I have made corresponding changes to the documentation
- [ ] My changes generate no new warnings
- [ ] I have added tests that prove my fix is effective or that my feature works
- [ ] New and existing unit tests pass locally with my changes
- [ ] Any dependent changes have been merged and published

## Additional Notes
Any additional information reviewers should know.
```

### 3. Size Matters

**Keep PRs small and focused!**

✅ **Good PR Size:**
- 200-400 lines of code (including tests)
- Single feature or bug fix
- Can be reviewed in 15-30 minutes

❌ **Too Large:**
- 1000+ lines of code
- Multiple unrelated changes
- Takes hours to review

**Tips for large changes:**
- Break into smaller, sequential PRs
- Use stacked PRs (PR2 builds on PR1)
- Create a tracking issue with subtasks

## Reviewing Pull Requests

### The Review Process

1. **Understand the context**
   - Read the PR description
   - Review linked issues
   - Understand the problem being solved

2. **Check out the code locally**
   ```bash
   # Fetch PR branch
   git fetch origin pull/123/head:pr-123
   git checkout pr-123
   
   # Or use GitHub CLI
   gh pr checkout 123
   ```

3. **Review the changes**
   - Read through the diff
   - Look for logic errors
   - Check edge cases
   - Verify tests
   - Check documentation

4. **Test the changes**
   ```bash
   # Run tests
   npm test
   
   # Build the project
   npm run build
   
   # Manual testing
   npm start
   ```

5. **Leave feedback**
   - Be constructive and kind
   - Explain the "why" behind suggestions
   - Distinguish between "must fix" and "nice to have"

### What to Look For

#### Code Quality

```javascript
// ❌ Hard to understand
function p(a,b){return a.filter(x=>x.id===b)[0]}

// ✅ Clear and readable
function findUserById(users, userId) {
  return users.find(user => user.id === userId);
}
```

#### Error Handling

```javascript
// ❌ No error handling
async function getUser(id) {
  const response = await fetch(`/api/users/${id}`);
  return response.json();
}

// ✅ Proper error handling
async function getUser(id) {
  try {
    const response = await fetch(`/api/users/${id}`);
    if (!response.ok) {
      throw new Error(`HTTP error! status: ${response.status}`);
    }
    return await response.json();
  } catch (error) {
    console.error('Failed to fetch user:', error);
    throw error;
  }
}
```

#### Security Issues

- SQL injection vulnerabilities
- XSS vulnerabilities
- Exposed secrets or credentials
- Missing input validation
- Insecure dependencies

#### Performance

- Unnecessary loops
- Memory leaks
- N+1 query problems
- Large bundle sizes
- Unoptimized algorithms

#### Tests

```javascript
// ✅ Good test
describe('calculateTotal', () => {
  it('should sum array of numbers', () => {
    expect(calculateTotal([1, 2, 3])).toBe(6);
  });
  
  it('should return 0 for empty array', () => {
    expect(calculateTotal([])).toBe(0);
  });
  
  it('should handle negative numbers', () => {
    expect(calculateTotal([-1, 2, -3])).toBe(-2);
  });
});
```

### Providing Feedback

#### Types of Comments

Use prefixes to indicate severity:

- **MUST:** Critical issue that must be fixed
- **SHOULD:** Important suggestion
- **NIT:** Minor nitpick (nice to have)
- **QUESTION:** Asking for clarification
- **PRAISE:** Positive feedback

#### Examples

**Critical (MUST fix):**
```
MUST: This function is vulnerable to SQL injection.
Use parameterized queries instead:

// Current
db.query(`SELECT * FROM users WHERE id = ${userId}`)

// Better
db.query('SELECT * FROM users WHERE id = ?', [userId])
```

**Important (SHOULD change):**
```
SHOULD: This function should handle the case when user is null.
Consider adding a guard clause at the beginning.
```

**Nitpick:**
```
NIT: Consider using const instead of let here since the value 
never changes.
```

**Question:**
```
QUESTION: Why did we choose to use a Set instead of an Array here?
Is it for performance reasons?
```

**Praise:**
```
PRAISE: Great job handling all the edge cases! The tests are 
comprehensive and well-written.
```

### Review Comments Best Practices

✅ **Good Feedback:**

```
The error handling here could be improved. Currently, if the API 
returns a 404, the app crashes. Consider adding a try-catch block 
and returning a user-friendly error message.

Example:
try {
  const data = await fetchUser(id);
  return data;
} catch (error) {
  if (error.status === 404) {
    return { error: 'User not found' };
  }
  throw error;
}
```

❌ **Poor Feedback:**

```
This is wrong.
```

```
You should fix this.
```

```
I don't like this approach.
```

### The Reviewer's Code of Conduct

1. **Be kind and respectful**
   - Remember there's a human on the other side
   - Assume positive intent
   - Praise good work

2. **Be specific**
   - Point to exact lines
   - Provide examples
   - Explain the why

3. **Be timely**
   - Review within 24 hours
   - Don't block others' work

4. **Be constructive**
   - Suggest solutions, not just problems
   - Teach, don't criticize
   - Focus on the code, not the person

5. **Be thorough**
   - Test the changes
   - Check edge cases
   - Verify tests

## Responding to Review Comments

### As the PR Author

1. **Stay professional**
   - Don't take feedback personally
   - It's about improving the code

2. **Ask for clarification**
   - If you don't understand a comment, ask

3. **Discuss respectfully**
   - If you disagree, explain your reasoning
   - Be open to learning

4. **Mark conversations as resolved**
   - After addressing feedback
   - Or when discussion is complete

5. **Update the PR**
   - Push new commits to address feedback
   - Or use `git commit --amend` for small fixes

### Example Responses

**Agreeing with feedback:**
```
Good catch! Fixed in abc123.
```

**Asking for clarification:**
```
Could you elaborate on what you mean by "edge case"? 
I want to make sure I understand the concern.
```

**Respectful disagreement:**
```
I considered that approach, but went with this one because 
[reason]. However, I'm open to changing it if you think 
the benefits outweigh the tradeoffs. What do you think?
```

## PR Workflow States

### Draft PRs

Use draft PRs for work in progress:

```
[WIP] feat(auth): add OAuth2 authentication
```

- Signals it's not ready for review
- Useful for early feedback
- Can share progress with team

### Request Changes

Reviewer requests changes before approval:

- **Author**: Make requested changes
- **Author**: Push updates
- **Author**: Re-request review
- **Reviewer**: Review again

### Approve

Reviewer approves the PR:

- PR is ready to merge
- Must meet all requirements
- All discussions resolved

### Merge

Merge strategies:

#### 1. Merge Commit
```
Preserves all commits + creates merge commit
      
main:     A---B---C-------M
               \         /
feature:        D---E---F
```

#### 2. Squash and Merge
```
Combines all commits into one

main:     A---B---C---D'
               \
feature:        D---E---F (deleted)
```

#### 3. Rebase and Merge
```
Replays commits on top of main

main:     A---B---C---D---E---F
```

**When to use:**
- **Merge commit**: Want to preserve full history
- **Squash**: Want clean history, many small commits
- **Rebase**: Want linear history, already clean commits

## Automated Checks

### CI/CD Integration

Set up automated checks:

- ✅ Tests must pass
- ✅ Linting must pass
- ✅ Build must succeed
- ✅ Code coverage threshold met
- ✅ Security scans clean

Example GitHub Actions workflow:

```yaml
name: PR Checks

on: [pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Install dependencies
        run: npm install
      - name: Run tests
        run: npm test
      - name: Run linter
        run: npm run lint
      - name: Build
        run: npm run build
```

### Code Review Tools

- **Danger.js**: Automate common review tasks
- **CodeClimate**: Automated code review
- **SonarQube**: Code quality and security
- **Codecov**: Code coverage tracking

## Practice Exercises

### Exercise 1: Create a PR

1. Create a feature branch
2. Make a small change
3. Push to GitHub
4. Create a pull request with good description
5. Request review from a teammate

### Exercise 2: Review a PR

1. Find an open PR
2. Check out the code locally
3. Test the changes
4. Leave constructive feedback
5. Approve or request changes

### Exercise 3: Handle Feedback

1. Receive review comments
2. Address each comment
3. Push updates
4. Respond to reviewers
5. Get approval and merge

## Common PR Mistakes

### 1. Too Large

**Problem:** 2000 line PR that changes everything

**Solution:** Break into smaller PRs

### 2. Poor Description

**Problem:** "fixed stuff"

**Solution:** Write detailed description with context

### 3. No Tests

**Problem:** New feature without tests

**Solution:** Always add tests for new code

### 4. Breaking Changes

**Problem:** Changed API without updating consumers

**Solution:** Check for breaking changes, update dependents

### 5. Merge Conflicts

**Problem:** Branch is way behind main

**Solution:** Keep feature branch up to date

```bash
git checkout feature/my-branch
git fetch origin
git merge origin/main
# Resolve conflicts
git push
```

## PR Review Checklist

### For Authors

Before requesting review:
- [ ] Tests added/updated
- [ ] Tests pass locally
- [ ] Code linted/formatted
- [ ] Documentation updated
- [ ] Self-reviewed changes
- [ ] No debugging code
- [ ] Branch up to date with main
- [ ] Description is clear and complete

### For Reviewers

During review:
- [ ] Understand the context
- [ ] Check out and test locally
- [ ] Review logic and correctness
- [ ] Check for edge cases
- [ ] Verify tests are adequate
- [ ] Check for security issues
- [ ] Verify documentation
- [ ] Leave constructive feedback

## Advanced Topics

### Stacked PRs

When changes depend on each other:

```
PR1: feature/add-user-model → main
PR2: feature/add-user-api → feature/add-user-model
PR3: feature/add-user-ui → feature/add-user-api
```

Merge order: PR1 → PR2 → PR3

### Review Apps

Deploy PR to temporary environment for testing:

```yaml
# .github/workflows/review-app.yml
name: Deploy Review App

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  deploy:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      - name: Deploy to Heroku
        run: |
          # Deploy to review-app-pr-${{ github.event.number }}
```

## Summary

Great pull requests:
- Are small and focused
- Have clear descriptions
- Include tests
- Are easy to review
- Address feedback professionally

Great reviews:
- Are timely and thorough
- Are constructive and kind
- Focus on the code, not the person
- Teach and share knowledge

Remember: Code review is collaboration, not criticism!
