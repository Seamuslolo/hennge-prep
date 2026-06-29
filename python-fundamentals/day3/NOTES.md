# Git PR and commands
## Conflict testing
1. I created a new branch and committed & pushed the changes on it
2. Then I switch back to the main branch and created an marge conflict deliberately 
3. Surprisedly I resolved the conflict (by accepting current changes on the pull request) on Github, because I expected this will be done on my code editor

## Git commands used
### git restore file_path
1. When we want to discard uncommittd changes, and restore a specific back to the latest commit
```
git status
```
Copy and paste the intended file path to restore
```
git restore file_path
```
### git stash
2. Temporarily saves staged changes and leaves the untracked files in the working directory, so switching branches safely without committing.
```
git status
git stash + -u when files or folders is untracked
git switch main
git pull
git switch myBranch
git stash pop
```
Note that git stash lives ONLY locally.

### git revert
3. If a commit is already in history and causes a bug, git revert will create a new commit that undoes only that commit’s changes, without deleting or changing any later commits.
identify the commit we wa
```
git log --oneline

git revert <commit_hash>

# if editor opens:
# save & exit

git status

git log --oneline

git push

```
### git reset 
3. git reset moves the current branch pointer to a previous commit, optionally changing or discarding the working directory and staging area depending on the mode.

Move the pointer to B, but keep all the changes comes after B staged, ready to recommit.
```
git reset --soft B
```
Basically the same as the upon line, but it keeps the changes after B unstaged 
```
git reset B / git reset --mixed B
```
Move to B and discards all committed changes 
```
git reset --hard B
```
### git rescue
Check all commit even those one without a branch
```
git reflog
```
A rescue branch just points to an old commit, and that commit already includes its entire history.
```
git switch -c rescue branch_hash
```


## TODO
Record ~3 min explaining the difference between revert and reset in your own words. Teaching it back is how it sets.

git reset is used when working locally to move the current branch back to a previous commit and discard or reorganize commits before they are shared, effectively rewriting history to clean up work. 
git revert is used in shared or production branches to safely undo a specific commit by creating a new commit that reverses its changes, preserving the project history and avoiding disruption for other developers.

review git revert / rescue / reset again, creating a new git repo to test it

test 1
test 2