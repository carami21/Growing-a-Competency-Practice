# Practice Exercises

This directory contains example files you can use to practice Git and GitHub workflows.

## Files

### calculator.py
A simple Python calculator module that you can use to practice:
- Creating feature branches
- Making atomic commits
- Creating pull requests
- Adding tests

**Practice Ideas:**
1. Add new operations (power, modulo, etc.)
2. Add input validation
3. Add unit tests
4. Improve error handling

### config.md
A configuration file perfect for practicing merge conflicts.

**Practice Ideas:**
1. Create two branches from main
2. Modify the same settings differently in each branch
3. Merge one branch
4. Try to merge the second branch (conflict!)
5. Practice resolving conflicts

## General Practice Workflow

### 1. Fork and Clone
```bash
# Fork this repository on GitHub, then:
git clone https://github.com/YOUR-USERNAME/Growing-a-Competency-Practice.git
cd Growing-a-Competency-Practice
```

### 2. Create a Feature Branch
```bash
git checkout -b feature/add-calculator-power
```

### 3. Make Changes
Edit one of the example files:
```python
# In calculator.py, add:
def power(a, b):
    """Raise a to the power of b."""
    return a ** b
```

### 4. Commit with Good Message
```bash
git add examples/calculator.py
git commit -m "feat(calculator): add power function

Add function to calculate powers.
Useful for scientific calculations."
```

### 5. Push and Create PR
```bash
git push origin feature/add-calculator-power
# Then create PR on GitHub
```

## Practice Scenarios

### Scenario 1: Perfect Commits
1. Add multiple features to calculator.py
2. Make each feature a separate commit
3. Use proper commit message format
4. Review your history with `git log`

### Scenario 2: Interactive Rebase
1. Make several small commits
2. Use `git rebase -i HEAD~5` to clean them up
3. Squash related commits
4. Reword commit messages

### Scenario 3: Merge Conflicts
1. Create branch A and modify config.md (change Port to 8080)
2. Create branch B and modify config.md (change Port to 9000)
3. Merge branch A to main
4. Try to merge branch B (conflict!)
5. Resolve the conflict

### Scenario 4: Cherry-Pick
1. Create a feature branch
2. Make several commits
3. Cherry-pick only one commit to main
4. Practice selective integration

### Scenario 5: Stash
1. Start making changes
2. Need to switch branches urgently
3. Use `git stash` to save work
4. Switch branches, do other work
5. Return and `git stash pop`

## Tips

- Don't be afraid to experiment - this is a practice repo!
- Use `git log --oneline --graph --all` to visualize history
- Try different Git commands and workflows
- Create your own practice scenarios
- Share your exercises with others

## Contributing

Found a good practice scenario? Add it here!
1. Fork the repo
2. Add your scenario
3. Create a pull request
4. Help others learn!

Happy practicing! 🚀
