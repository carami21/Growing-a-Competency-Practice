# Growing-a-Competency-Practice

A comprehensive practice repository to master GitHub workflows and Git best practices.

## 📚 Table of Contents

1. [Perfect Commits](#1-perfect-commits)
2. [Branching Strategy](#2-branching-strategy)
3. [Pull Request Reviews](#3-pull-request-reviews)
4. [Merge Conflicts](#4-merge-conflicts)
5. [Merge vs Rebase](#5-merge-vs-rebase)
6. [Releases and Tags](#6-releases-and-tags)
7. [Project Management](#7-project-management)

---

## 1. Perfect Commits

Learn how to write meaningful commits that tell a story.

### Best Practices

- **Write clear commit messages**: Start with a verb in present tense (Add, Fix, Update, Remove)
- **Keep commits atomic**: One logical change per commit
- **Use the commit message body**: Explain the "why" not just the "what"

### Commit Message Template

```
<type>: <short summary (50 chars max)>

<body - explain what and why (72 chars per line)>

<footer - references to issues, breaking changes>
```

### Types
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes (formatting, semicolons, etc.)
- `refactor`: Code refactoring
- `test`: Adding or updating tests
- `chore`: Maintenance tasks

### Practice Exercise

See [docs/perfect-commits.md](docs/perfect-commits.md) for hands-on exercises.

---

## 2. Branching Strategy

Master Git branching for effective collaboration.

### Common Branching Models

#### Git Flow
- `main`: Production-ready code
- `develop`: Integration branch for features
- `feature/*`: New features
- `hotfix/*`: Emergency fixes
- `release/*`: Release preparation

#### GitHub Flow (Simpler)
- `main`: Always deployable
- `feature/*`: All new work

### Branch Naming Conventions

```
feature/add-user-authentication
bugfix/fix-login-error
hotfix/patch-security-vulnerability
release/v1.2.0
```

### Practice Exercise

See [docs/branching.md](docs/branching.md) for detailed examples.

---

## 3. Pull Request Reviews

Learn effective code review practices.

### PR Best Practices

1. **Keep PRs small and focused**: Easier to review, less risk
2. **Write descriptive titles and descriptions**: Context is key
3. **Link related issues**: Use "Fixes #123" or "Closes #456"
4. **Request specific reviewers**: Tag domain experts
5. **Respond to feedback promptly**: Keep the conversation flowing

### PR Template

```markdown
## Description
Brief description of changes

## Type of Change
- [ ] Bug fix
- [ ] New feature
- [ ] Breaking change
- [ ] Documentation update

## Testing
How has this been tested?

## Checklist
- [ ] Code follows style guidelines
- [ ] Self-review completed
- [ ] Tests added/updated
- [ ] Documentation updated
```

### Practice Exercise

See [docs/pull-requests.md](docs/pull-requests.md) for review guidelines.

---

## 4. Merge Conflicts

Learn to handle and resolve merge conflicts like a pro.

### Common Causes
- Multiple people editing the same file
- Deleted files that others modified
- Renamed files

### Resolution Steps

1. **Identify the conflict**:
   ```bash
   git status
   ```

2. **Open conflicting files** and look for conflict markers:
   ```
   <<<<<<< HEAD
   Your changes
   =======
   Their changes
   >>>>>>> branch-name
   ```

3. **Resolve manually** or use a merge tool:
   ```bash
   git mergetool
   ```

4. **Mark as resolved**:
   ```bash
   git add <file>
   git commit
   ```

### Practice Exercise

See [docs/merge-conflicts.md](docs/merge-conflicts.md) for practice scenarios.

---

## 5. Merge vs Rebase

Understand when to merge and when to rebase.

### Merge

**Pros:**
- Preserves complete history
- Safe for shared branches
- Shows when features were integrated

**Cons:**
- Creates merge commits (can clutter history)

```bash
git checkout main
git merge feature-branch
```

### Rebase

**Pros:**
- Linear, clean history
- Easier to follow
- No merge commits

**Cons:**
- Rewrites history (dangerous on shared branches)
- Can lose context about when features were integrated

```bash
git checkout feature-branch
git rebase main
```

### Golden Rule

**Never rebase public/shared branches!** Only rebase your local feature branches.

### When to Use Each

- **Merge**: For integrating feature branches into main/develop
- **Rebase**: For updating your feature branch with latest main changes

### Practice Exercise

See [docs/merge-vs-rebase.md](docs/merge-vs-rebase.md) for examples.

---

## 6. Releases and Tags

Learn semantic versioning and release management.

### Semantic Versioning (SemVer)

Format: `MAJOR.MINOR.PATCH` (e.g., `v1.2.3`)

- **MAJOR**: Breaking changes
- **MINOR**: New features (backward compatible)
- **PATCH**: Bug fixes (backward compatible)

### Creating Tags

```bash
# Lightweight tag
git tag v1.0.0

# Annotated tag (recommended)
git tag -a v1.0.0 -m "Release version 1.0.0"

# Push tags
git push origin v1.0.0
# Or push all tags
git push origin --tags
```

### GitHub Releases

1. Go to repository → Releases → Draft a new release
2. Choose or create a tag
3. Fill in release notes
4. Attach binaries/assets (if needed)
5. Publish release

### Practice Exercise

See [docs/releases-tags.md](docs/releases-tags.md) for detailed workflows.

---

## 7. Project Management

Use GitHub's built-in project management tools.

### Issues

- **Bug reports**: Template for reporting bugs
- **Feature requests**: Template for requesting features
- **Tasks**: Breaking down work

### Labels

Organize issues with labels:
- `bug`: Something isn't working
- `enhancement`: New feature or request
- `documentation`: Documentation improvements
- `good first issue`: Good for newcomers
- `help wanted`: Extra attention needed

### Projects (Kanban Boards)

Track work with columns:
- **Backlog**: Future work
- **To Do**: Ready to work on
- **In Progress**: Currently being worked on
- **Review**: Awaiting review
- **Done**: Completed

### Milestones

Group related issues for release planning:
```
v1.0.0 Milestone
├── Issue #1: User authentication
├── Issue #2: Database setup
└── Issue #3: API endpoints
```

### Practice Exercise

See [docs/project-management.md](docs/project-management.md) for setup guide.

---

## 🚀 Getting Started

1. **Fork this repository** to your own GitHub account
2. **Clone your fork** locally:
   ```bash
   git clone https://github.com/YOUR-USERNAME/Growing-a-Competency-Practice.git
   cd Growing-a-Competency-Practice
   ```
3. **Follow the exercises** in the `docs/` folder
4. **Practice each workflow** in this repository

---

## 📖 Additional Resources

- [Git Documentation](https://git-scm.com/doc)
- [GitHub Docs](https://docs.github.com/)
- [Pro Git Book](https://git-scm.com/book/en/v2)
- [Atlassian Git Tutorials](https://www.atlassian.com/git/tutorials)

---

## 🤝 Contributing

This is a practice repository! Feel free to:
- Open issues for practice
- Create PRs to practice workflows
- Experiment with branches and merges

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

---

## 📝 License

This is a practice repository for educational purposes.
