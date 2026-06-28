## Git PR and commands
# Conflict testing
1. I created a new branch and committed & pushed the changes on it
2. Then I switch back to the main branch and created an marge conflict deliberately 
3. Surprisedly I resolved the conflict (by accepting current changes on the pull request) on Github, because I expected this will be done on my code editor

# Git commands used
1. When we want to discard uncommittd changes, and restore a specific back to the latest commit
```
git status
```
Copy and paste the intended file path to restore
```
git restore file_path
```
2. When working on a branches we created and we want to leave the changes uncommited and saved only in the branches, we can do:
```
git status
git stash / add -u when files or folders is untracked
git switch main
git pull
git switch myBranch
git stash pop
```
Note that git stash lives ONLY locally.

# TODO
Record ~3 min explaining the difference between revert and reset in your own words. Teaching it back is how it sets.


