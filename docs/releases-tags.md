# Releases and Tags Guide

## What are Tags?

Tags are references that point to specific commits in Git history. They're typically used to mark release points (v1.0.0, v2.0.0, etc.).

## Why Use Tags?

- **Mark important milestones**: Releases, major features
- **Easy reference**: Jump to specific versions quickly
- **Deployment**: Deploy specific tagged versions
- **Changelog**: Generate release notes between tags
- **Rollback**: Easy to revert to tagged versions

## Types of Tags

### Lightweight Tags

Simple pointer to a commit:

```bash
git tag v1.0.0
```

**Use for:**
- Temporary marks
- Personal bookmarks
- Quick references

### Annotated Tags (Recommended)

Full Git objects with metadata:

```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
```

**Includes:**
- Tagger name and email
- Date
- Message
- Can be signed and verified

**Use for:**
- Official releases
- Public tags
- Shared tags

## Semantic Versioning (SemVer)

### Format: MAJOR.MINOR.PATCH

```
v1.2.3
│ │ │
│ │ └─ PATCH: Bug fixes (backward compatible)
│ └─── MINOR: New features (backward compatible)
└───── MAJOR: Breaking changes
```

### Examples

| Version | Change |
|---------|--------|
| 1.0.0 | Initial release |
| 1.0.1 | Bug fix |
| 1.1.0 | New feature (no breaking changes) |
| 1.1.1 | Another bug fix |
| 2.0.0 | Breaking change |

### Pre-release Versions

```
1.0.0-alpha.1    # Alpha release
1.0.0-beta.1     # Beta release
1.0.0-rc.1       # Release candidate
```

### Build Metadata

```
1.0.0+20230615   # Build date
1.0.0+build.123  # Build number
```

## Creating Tags

### Create Annotated Tag

```bash
# Tag current commit
git tag -a v1.0.0 -m "Release 1.0.0: Initial stable release"

# Tag specific commit
git tag -a v1.0.0 abc123 -m "Release 1.0.0"

# Tag with detailed message
git tag -a v1.0.0
# Opens editor for multi-line message
```

### Create Lightweight Tag

```bash
# Tag current commit
git tag v1.0.0

# Tag specific commit
git tag v1.0.0 abc123
```

### Signed Tags

For extra security:

```bash
# Create GPG-signed tag
git tag -s v1.0.0 -m "Signed release 1.0.0"

# Verify signature
git tag -v v1.0.0
```

## Viewing Tags

### List Tags

```bash
# List all tags
git tag

# List tags matching pattern
git tag -l "v1.*"
git tag -l "v2.0.*"

# List with messages
git tag -n

# List with full details
git show v1.0.0
```

### Show Tag Details

```bash
# Show commit that tag points to
git show v1.0.0

# Show just the tag object
git cat-file -p v1.0.0

# Show commits since tag
git log v1.0.0..HEAD

# Show difference between tags
git log v1.0.0..v1.1.0
```

## Pushing Tags

### Push Single Tag

```bash
# Push specific tag
git push origin v1.0.0
```

### Push All Tags

```bash
# Push all tags at once
git push origin --tags

# Or
git push --tags
```

### Push and Create Tag

```bash
# Create and push in one go
git tag -a v1.0.0 -m "Release 1.0.0" && git push origin v1.0.0
```

## Deleting Tags

### Delete Local Tag

```bash
git tag -d v1.0.0
```

### Delete Remote Tag

```bash
# Method 1
git push origin --delete v1.0.0

# Method 2
git push origin :refs/tags/v1.0.0
```

### Delete Local and Remote

```bash
git tag -d v1.0.0
git push origin --delete v1.0.0
```

## GitHub Releases

### What are GitHub Releases?

GitHub Releases add extra features on top of Git tags:
- Release notes
- Binary assets (executables, archives)
- Automated changelog
- Draft releases
- Pre-releases

### Creating a Release via GitHub UI

1. **Navigate to repository**
   - Go to your repository on GitHub

2. **Click "Releases"**
   - In the right sidebar
   - Or go to: `github.com/user/repo/releases`

3. **Click "Draft a new release"**

4. **Fill in the form:**
   - **Tag version**: e.g., `v1.0.0`
   - **Release title**: e.g., `Version 1.0.0 - Initial Release`
   - **Description**: Release notes (what's new, fixed, etc.)
   - **Attach binaries**: Optional files to include
   - **Pre-release**: Check if this is a pre-release
   - **Set as latest**: Check if this should be the latest release

5. **Publish release**

### Creating a Release via GitHub CLI

```bash
# Install GitHub CLI first
# https://cli.github.com/

# Create release
gh release create v1.0.0 \
  --title "Version 1.0.0" \
  --notes "Initial stable release"

# Create release with assets
gh release create v1.0.0 \
  --title "Version 1.0.0" \
  --notes "Initial stable release" \
  dist/*.zip dist/*.tar.gz

# Create pre-release
gh release create v2.0.0-beta.1 \
  --title "Version 2.0.0 Beta 1" \
  --notes "Beta release for testing" \
  --prerelease

# Create draft release
gh release create v1.0.0 \
  --title "Version 1.0.0" \
  --notes "Draft release" \
  --draft
```

### Creating a Release via API

```bash
# Using curl
curl -X POST \
  -H "Authorization: token YOUR_TOKEN" \
  -H "Accept: application/vnd.github.v3+json" \
  https://api.github.com/repos/USER/REPO/releases \
  -d '{
    "tag_name": "v1.0.0",
    "name": "Version 1.0.0",
    "body": "Release notes here",
    "draft": false,
    "prerelease": false
  }'
```

## Release Notes Best Practices

### Structure

```markdown
## Version 1.2.0 - 2024-01-15

### 🎉 New Features
- Added user authentication with OAuth2
- Implemented dark mode
- Added export to PDF functionality

### 🐛 Bug Fixes
- Fixed login redirect loop (#123)
- Resolved memory leak in image processing (#145)
- Fixed timezone display issue (#167)

### 🔄 Changes
- Updated dependencies to latest versions
- Improved error messages
- Optimized database queries

### ⚠️ Breaking Changes
- Removed deprecated API endpoints
- Changed configuration file format

### 📝 Documentation
- Added API documentation
- Updated installation guide
- Added troubleshooting section

### 🙏 Contributors
Thanks to @user1, @user2, and @user3 for their contributions!
```

### Auto-generate Release Notes

GitHub can auto-generate release notes:

```bash
# Via GitHub CLI
gh release create v1.0.0 --generate-notes

# Or on GitHub UI: check "Generate release notes"
```

## Release Workflow

### Development Release Workflow

```bash
# 1. Finish feature development
git checkout develop
git merge feature/new-feature

# 2. Create release branch
git checkout -b release/v1.2.0

# 3. Update version numbers
# - package.json
# - version files
# - documentation
git commit -am "chore: bump version to 1.2.0"

# 4. Test thoroughly
npm run test
npm run build
# Manual testing

# 5. Merge to main
git checkout main
git merge --no-ff release/v1.2.0

# 6. Create tag
git tag -a v1.2.0 -m "Release version 1.2.0

New Features:
- Feature A
- Feature B

Bug Fixes:
- Fix X
- Fix Y"

# 7. Push
git push origin main
git push origin v1.2.0

# 8. Merge back to develop
git checkout develop
git merge --no-ff release/v1.2.0
git push origin develop

# 9. Create GitHub Release
gh release create v1.2.0 \
  --title "Version 1.2.0" \
  --notes-file CHANGELOG.md
```

### Hotfix Release Workflow

```bash
# 1. Create hotfix branch from main
git checkout main
git checkout -b hotfix/v1.2.1

# 2. Fix the bug
# ... make changes ...
git commit -am "fix: resolve critical security issue"

# 3. Update version
# ... update version files ...
git commit -am "chore: bump version to 1.2.1"

# 4. Test
npm run test

# 5. Merge to main
git checkout main
git merge --no-ff hotfix/v1.2.1

# 6. Tag
git tag -a v1.2.1 -m "Hotfix 1.2.1: Security patch"

# 7. Push
git push origin main
git push origin v1.2.1

# 8. Merge to develop
git checkout develop
git merge --no-ff hotfix/v1.2.1
git push origin develop

# 9. Create release
gh release create v1.2.1 \
  --title "Version 1.2.1 (Hotfix)" \
  --notes "Security patch for CVE-2024-XXXX"
```

## Changelog Management

### Manual Changelog

Keep a `CHANGELOG.md` file:

```markdown
# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/),
and this project adheres to [Semantic Versioning](https://semver.org/).

## [Unreleased]

### Added
- New feature coming soon

## [1.2.0] - 2024-01-15

### Added
- User authentication
- Dark mode support

### Fixed
- Login redirect issue (#123)

### Changed
- Updated dependencies

## [1.1.0] - 2024-01-01

### Added
- Export functionality

## [1.0.0] - 2023-12-15

### Added
- Initial release
```

### Automated Changelog

Use tools to generate changelog from commits:

```bash
# Install conventional-changelog
npm install -g conventional-changelog-cli

# Generate changelog
conventional-changelog -p angular -i CHANGELOG.md -s

# Or add to package.json
{
  "scripts": {
    "changelog": "conventional-changelog -p angular -i CHANGELOG.md -s"
  }
}
```

## Version Bumping

### Manual Version Bump

```bash
# Update version in files
# package.json, setup.py, etc.

# Commit
git commit -am "chore: bump version to 1.2.0"

# Tag
git tag -a v1.2.0 -m "Release 1.2.0"
```

### Automated Version Bump

```bash
# Using npm (for Node.js projects)
npm version patch  # 1.0.0 -> 1.0.1
npm version minor  # 1.0.0 -> 1.1.0
npm version major  # 1.0.0 -> 2.0.0

# This automatically:
# 1. Updates package.json
# 2. Creates git tag
# 3. Commits the change

# Then push
git push origin main --tags
```

## Release Checklist

### Pre-release

- [ ] All features complete and tested
- [ ] All tests passing
- [ ] Code reviewed
- [ ] Documentation updated
- [ ] Version number updated
- [ ] Changelog updated
- [ ] Migration guides written (if breaking changes)

### Release

- [ ] Create release branch (if using Git Flow)
- [ ] Final testing
- [ ] Merge to main
- [ ] Create and push tag
- [ ] Create GitHub Release
- [ ] Build and upload artifacts
- [ ] Merge back to develop

### Post-release

- [ ] Announce release (blog, Twitter, etc.)
- [ ] Close related issues/milestones
- [ ] Update documentation site
- [ ] Monitor for issues
- [ ] Prepare hotfix if needed

## Advanced Topics

### Release Branches

For long-term support of multiple versions:

```
main
├── release/v1.x
├── release/v2.x
└── release/v3.x
```

Each release branch gets its own patches:
```bash
# Fix bug in v2.x
git checkout release/v2.x
git checkout -b hotfix/v2.1.5
# ... fix bug ...
git checkout release/v2.x
git merge hotfix/v2.1.5
git tag -a v2.1.5 -m "Hotfix 2.1.5"
```

### Signing Releases

For enhanced security:

```bash
# Sign tag with GPG
git tag -s v1.0.0 -m "Signed release 1.0.0"

# Sign commits
git commit -S -m "feat: add new feature"

# Configure Git to always sign
git config --global commit.gpgsign true
git config --global tag.gpgsign true
```

### Release Automation with GitHub Actions

```yaml
# .github/workflows/release.yml
name: Release

on:
  push:
    tags:
      - 'v*'

jobs:
  release:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v2
      
      - name: Build
        run: |
          npm install
          npm run build
      
      - name: Create Release
        uses: actions/create-release@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          tag_name: ${{ github.ref }}
          release_name: Release ${{ github.ref }}
          draft: false
          prerelease: false
      
      - name: Upload Assets
        uses: actions/upload-release-asset@v1
        env:
          GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
        with:
          upload_url: ${{ steps.create_release.outputs.upload_url }}
          asset_path: ./dist/app.zip
          asset_name: app.zip
          asset_content_type: application/zip
```

## Practice Exercises

### Exercise 1: Create Tags

```bash
# Create a test repo
mkdir tag-practice
cd tag-practice
git init

# Make some commits
echo "v1" > file.txt
git add file.txt
git commit -m "Initial commit"

# Create a lightweight tag
git tag v0.1.0

# Make more changes
echo "v2" > file.txt
git commit -am "Update to v2"

# Create an annotated tag
git tag -a v1.0.0 -m "First stable release"

# View tags
git tag
git show v1.0.0
```

### Exercise 2: Create GitHub Release

```bash
# Using GitHub CLI
gh release create v1.0.0 \
  --title "Version 1.0.0" \
  --notes "Initial release with basic features"

# List releases
gh release list

# View release
gh release view v1.0.0
```

### Exercise 3: Version Workflow

```bash
# Simulate a release workflow
git checkout -b release/v1.1.0
# Update version in files
git commit -am "chore: bump to v1.1.0"
git checkout main
git merge --no-ff release/v1.1.0
git tag -a v1.1.0 -m "Release 1.1.0"
git push origin main --tags
```

## Summary

- **Tags** mark important points in history
- **Semantic Versioning** provides clear version meaning
- **Annotated tags** are better for releases
- **GitHub Releases** add features on top of tags
- **Automate** where possible to reduce errors
- **Document** changes in changelog
- **Test thoroughly** before releasing

Good release management makes it easy to:
- Track what changed
- Deploy specific versions
- Rollback if needed
- Communicate with users

Start with simple tags and releases, then add automation as you grow!
