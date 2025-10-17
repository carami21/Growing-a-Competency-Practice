# Project Management with GitHub

## GitHub Project Management Tools

GitHub provides built-in tools for managing software projects:

1. **Issues** - Track bugs, features, and tasks
2. **Pull Requests** - Code review and collaboration
3. **Projects** - Kanban boards and roadmaps
4. **Milestones** - Group issues for releases
5. **Labels** - Categorize and filter issues
6. **Discussions** - Community conversations
7. **Wiki** - Documentation

## Issues

### What are Issues?

Issues are used to track:
- 🐛 Bug reports
- ✨ Feature requests
- 📋 Tasks
- 💬 Questions
- 📝 Documentation improvements

### Creating an Issue

**Via GitHub UI:**
1. Go to repository → Issues → New Issue
2. Fill in title and description
3. Add labels, assignees, projects, milestone
4. Submit issue

**Via GitHub CLI:**
```bash
# Create simple issue
gh issue create --title "Add user authentication" --body "We need OAuth2 login"

# Create with labels
gh issue create \
  --title "Fix login bug" \
  --body "Users can't log in" \
  --label "bug,high-priority"

# Create with assignment
gh issue create \
  --title "Update docs" \
  --body "Documentation needs updating" \
  --assignee "@me"
```

### Issue Templates

Create templates for consistent issue reporting.

**Bug Report Template** (`.github/ISSUE_TEMPLATE/bug_report.md`):
```markdown
---
name: Bug Report
about: Report a bug
title: '[BUG] '
labels: bug
assignees: ''
---

## Description
A clear description of the bug.

## Steps to Reproduce
1. Go to '...'
2. Click on '...'
3. See error

## Expected Behavior
What should happen?

## Actual Behavior
What actually happens?

## Screenshots
If applicable, add screenshots.

## Environment
- OS: [e.g., Windows 10]
- Browser: [e.g., Chrome 91]
- Version: [e.g., 1.2.0]

## Additional Context
Any other information.
```

**Feature Request Template** (`.github/ISSUE_TEMPLATE/feature_request.md`):
```markdown
---
name: Feature Request
about: Suggest a new feature
title: '[FEATURE] '
labels: enhancement
assignees: ''
---

## Problem
What problem does this solve?

## Proposed Solution
How should it work?

## Alternatives Considered
What other approaches did you consider?

## Additional Context
Any other information.
```

### Issue Best Practices

✅ **Good Issue:**
```markdown
## Bug: Login fails with valid credentials

**Description:**
Users are unable to log in even with correct username/password.
Error message: "Invalid credentials"

**Steps to Reproduce:**
1. Go to /login
2. Enter username: test@example.com
3. Enter password: correct-password
4. Click "Login"
5. See error message

**Expected:** User should be logged in
**Actual:** Error message appears

**Environment:**
- Version: 1.2.0
- Browser: Chrome 120
- OS: Windows 11

**Logs:**
```
Error: Authentication failed
  at login.js:45
```

**Related:** Might be related to #123
```

❌ **Poor Issue:**
```
login broken
```

### Linking Issues

Link related issues and PRs:

```markdown
## References
- Related to #123
- Blocks #456
- Blocked by #789
- Duplicate of #101

## Fixes
- Fixes #42
- Closes #43
- Resolves #44
```

When you merge a PR with "Fixes #42" in the description, issue #42 closes automatically.

## Labels

### Default Labels

GitHub provides default labels:
- `bug` - Something isn't working
- `documentation` - Documentation improvements
- `duplicate` - Duplicate issue
- `enhancement` - New feature
- `good first issue` - Good for newcomers
- `help wanted` - Extra attention needed
- `invalid` - Not valid
- `question` - Question
- `wontfix` - Won't be fixed

### Custom Labels

Create custom labels for your workflow:

**Priority:**
- 🔴 `priority: critical` - Must fix ASAP
- 🟠 `priority: high` - Important
- 🟡 `priority: medium` - Normal
- 🟢 `priority: low` - Nice to have

**Type:**
- `type: bug` - Bug fix
- `type: feature` - New feature
- `type: refactor` - Code improvement
- `type: test` - Testing
- `type: docs` - Documentation

**Status:**
- `status: blocked` - Blocked by something
- `status: in-progress` - Being worked on
- `status: ready` - Ready to work on
- `status: needs-review` - Needs review

**Area:**
- `area: frontend` - Frontend code
- `area: backend` - Backend code
- `area: database` - Database
- `area: api` - API

### Managing Labels

```bash
# List labels
gh label list

# Create label
gh label create "priority: high" \
  --description "High priority" \
  --color "FF0000"

# Edit label
gh label edit "priority: high" --color "FF6600"

# Delete label
gh label delete "old-label"
```

## Milestones

Group issues for releases or sprints.

### Creating Milestones

**Via GitHub UI:**
1. Go to Issues → Milestones → New Milestone
2. Enter title: "Version 1.2.0"
3. Set due date (optional)
4. Add description
5. Create milestone

**Via GitHub CLI:**
```bash
gh api repos/:owner/:repo/milestones \
  -f title="Version 1.2.0" \
  -f description="Release 1.2.0" \
  -f due_on="2024-03-01T00:00:00Z"
```

### Milestone Best Practices

```markdown
## Milestone: Version 1.2.0

**Goal:** Add user authentication and improve performance

**Due Date:** March 1, 2024

**Issues:**
- #10 Add OAuth2 login
- #11 Add password reset
- #12 Optimize database queries
- #13 Add caching layer

**Progress:** 2/4 complete (50%)
```

## Projects (Kanban Boards)

### Classic Projects vs New Projects

**Classic Projects:** Simple Kanban boards
**New Projects (Beta):** Advanced features, tables, roadmaps

### Creating a Project

**Via GitHub UI:**
1. Go to repository → Projects → New Project
2. Choose template or start blank
3. Add columns (To Do, In Progress, Done)
4. Add issues/PRs to board

### Project Templates

**Basic Kanban:**
```
📋 Backlog → 📝 To Do → 🏗️ In Progress → 👀 Review → ✅ Done
```

**Bug Triage:**
```
🐛 New → 🔍 Triage → ✅ Confirmed → 🛠️ In Progress → ✅ Done
```

**Release Planning:**
```
💡 Ideas → 📋 Planned → 🏗️ In Development → 🧪 Testing → 🚀 Released
```

### Automating Projects

Set up automation:
- Auto-add new issues to "To Do"
- Move to "In Progress" when assigned
- Move to "Review" when PR created
- Move to "Done" when PR merged

**Example Automation** (`.github/workflows/project-automation.yml`):
```yaml
name: Project Automation

on:
  issues:
    types: [opened]
  pull_request:
    types: [opened, closed]

jobs:
  add-to-project:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/add-to-project@v0.3.0
        with:
          project-url: https://github.com/users/USERNAME/projects/1
          github-token: ${{ secrets.ADD_TO_PROJECT_PAT }}
```

## Discussions

Enable Discussions for community engagement:

**Use Cases:**
- 💬 General questions
- 💡 Ideas and feature suggestions
- 📢 Announcements
- 🙏 Q&A
- 🎉 Show and tell

**Enable Discussions:**
1. Go to Settings → Features
2. Check "Discussions"
3. Set up categories

## GitHub Actions for Project Management

### Auto-assign Issues

```yaml
# .github/workflows/auto-assign.yml
name: Auto Assign

on:
  issues:
    types: [opened]

jobs:
  assign:
    runs-on: ubuntu-latest
    steps:
      - uses: pozil/auto-assign-issue@v1
        with:
          assignees: user1,user2,user3
          numOfAssignee: 1
```

### Stale Issue Management

```yaml
# .github/workflows/stale.yml
name: Close Stale Issues

on:
  schedule:
    - cron: '0 0 * * *'

jobs:
  stale:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/stale@v5
        with:
          stale-issue-message: 'This issue is stale and will be closed soon.'
          close-issue-message: 'Closed due to inactivity.'
          days-before-stale: 30
          days-before-close: 7
          stale-issue-label: 'stale'
```

### Issue Labeler

```yaml
# .github/workflows/label.yml
name: Label Issues

on:
  issues:
    types: [opened]

jobs:
  label:
    runs-on: ubuntu-latest
    steps:
      - uses: github/issue-labeler@v2.5
        with:
          repo-token: ${{ secrets.GITHUB_TOKEN }}
          configuration-path: .github/labeler.yml
```

**Labeler Config** (`.github/labeler.yml`):
```yaml
bug:
  - '.*\[BUG\].*'
  - '.*bug.*'
  - '.*error.*'

feature:
  - '.*\[FEATURE\].*'
  - '.*feature request.*'

documentation:
  - '.*\[DOCS\].*'
  - '.*documentation.*'
```

## Pull Request Templates

Create a default PR template (`.github/pull_request_template.md`):

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Related Issues
Fixes #

## Changes Made
- Change 1
- Change 2
- Change 3

## Testing
- [ ] Unit tests added/updated
- [ ] Integration tests added/updated
- [ ] Manual testing completed

## Screenshots (if applicable)

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Comments added for complex code
- [ ] Documentation updated
- [ ] No new warnings
- [ ] Tests pass locally
```

## Code Owners

Define who reviews specific parts of the codebase (`.github/CODEOWNERS`):

```
# Global owners
*       @team-leads

# Frontend team owns UI
/src/ui/    @frontend-team
*.css       @frontend-team
*.jsx       @frontend-team

# Backend team owns API
/src/api/   @backend-team
*.py        @backend-team

# DevOps owns CI/CD
/.github/workflows/    @devops-team
/docker/               @devops-team

# Docs team owns documentation
/docs/      @docs-team
*.md        @docs-team

# Security team must approve auth changes
/src/auth/  @security-team
```

## Branch Protection Rules

Protect important branches:

**Settings → Branches → Add rule**

Recommended settings for `main`:

- ✅ **Require pull request reviews**
  - Number of approvals: 1-2
  - Dismiss stale reviews
  - Require review from code owners

- ✅ **Require status checks to pass**
  - Require branches to be up to date
  - Add specific checks (tests, linting)

- ✅ **Require conversation resolution**

- ✅ **Require signed commits** (optional)

- ✅ **Include administrators**

- ✅ **Restrict who can push**

- ✅ **Allow force pushes**: Never

- ✅ **Allow deletions**: Never

## Team Workflows

### Agile Sprint Workflow

```markdown
## Sprint Planning
1. Create milestone for sprint
2. Add issues to milestone
3. Set sprint due date
4. Estimate story points (labels)
5. Assign issues to team members

## During Sprint
1. Move issues on project board
2. Daily standups (Discussions)
3. Update issue status
4. Create PRs linking issues

## Sprint Review
1. Demo completed work
2. Close completed issues
3. Move unfinished to next sprint
4. Retrospective discussion

## Sprint Retrospective
1. What went well?
2. What can improve?
3. Action items (create issues)
```

### Release Workflow

```markdown
## Release Planning
1. Create milestone for version
2. Add issues/features
3. Set target date
4. Track progress

## Development
1. Create feature branches
2. Link PRs to issues
3. Review and merge

## Pre-release
1. Create release branch
2. Final testing
3. Update changelog
4. Version bump

## Release
1. Merge to main
2. Create tag
3. Create GitHub Release
4. Close milestone
5. Announce release
```

## Best Practices

### 1. Issue Management

- Use descriptive titles
- Provide context and details
- Use templates
- Add appropriate labels
- Link related issues
- Keep issues focused (one topic per issue)
- Close stale issues

### 2. Project Organization

- Use projects for tracking
- Keep boards up to date
- Automate where possible
- Regular grooming/cleanup
- Clear column definitions

### 3. Communication

- Comment on issues for updates
- Use @mentions for notifications
- Use Discussions for general topics
- Keep conversations professional
- Document decisions

### 4. Automation

- Set up GitHub Actions
- Auto-label issues
- Auto-assign reviewers
- Notify on important events
- Generate reports

## Practice Exercises

### Exercise 1: Set Up Issue Templates

1. Create `.github/ISSUE_TEMPLATE/bug_report.md`
2. Create `.github/ISSUE_TEMPLATE/feature_request.md`
3. Test by creating a new issue

### Exercise 2: Create a Project Board

1. Create a new project
2. Add columns: To Do, In Progress, Done
3. Add existing issues to board
4. Move issues between columns

### Exercise 3: Configure Branch Protection

1. Go to Settings → Branches
2. Add protection rule for `main`
3. Require PR reviews
4. Require status checks
5. Test by trying to push directly

### Exercise 4: Set Up Labels

1. Create priority labels (high, medium, low)
2. Create type labels (bug, feature, docs)
3. Create area labels (frontend, backend, api)
4. Apply labels to existing issues

## Summary

GitHub provides powerful project management tools:

- **Issues** for tracking work
- **Labels** for organization
- **Milestones** for releases
- **Projects** for visualization
- **Templates** for consistency
- **Automation** for efficiency

Good project management:
- Keeps team organized
- Improves communication
- Tracks progress
- Reduces friction
- Increases productivity

Start simple and add complexity as needed!
