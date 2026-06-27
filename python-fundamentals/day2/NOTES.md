## Git Set up

# 1. identity (your real name — it shows on every commit)
git config --global user.name "Seamus Wong"
git config --global user.email "loloseamus0925@gmail.com"
git config --global init.defaultBranch main   # so local matches GitHub's "main"

# 2. turn this folder into a local git repo
git init

# 3. a Python .gitignore so junk never gets committed
printf ".venv\n__pycache__/\n*.pyc\n.pytest_cache\n.env\n*.db\n" > .gitignore

# 4. a starter README and your first real commit
echo "# HENNGE Prep" > README.md
git add .
git commit -m "chore: initial commit with gitignore and readme"

# 5. look at what you just did
git status
git log --oneline

# After craete new repo on github.com
git remote add origin https://github.com/Seamuslolo/hennge-prep.git
git 


# Repoint the remost at the new repo
git remote set-url origin git@github.com:Seamuslolo/hennge-prep.git
git remote -v used to check which git repo is this local porjet connected to 

# Common commnads used
- git log --oneline shows shows the current branch's history, add -all to see across all branches  
- git status checks what is staged, motified in the local dir, and if the git repo is up-to-date with the remote repo 
- git remote -v used for check which git repo is this local porjet connected to 

- git ls-files | grep -E "\.venv|pytest_cache"
show all files on lcoal git repo, and filter the ouput list, -E enables | or operation.

- cp file.txt backup.txt or cp -r folder1 back_folder2 (copy folder with its content)
- rm file.txt or rm -rf folder (remove everything inside the folder)
- cat file.txt
- less large_file.txt 
- grep "specific_word" file.txt (optional: -i ignore cases differ)
- find . -name "file_name.py" (search the current folder and its subfolder for filename.py)

# Git workflow
git switch main
git pull 

git switch -c feature/add-search 
or fix/bug-name

- Repeat until code is approved
git add -A 
git commit -m "feat: add sign up page"
git push -u origin feature/add-search

- Clean up
git switch main 
git pull
git branch -d fix/empty-file-guard

- Simple workflow
make sure newest version on local
create branch and push it
commit and push until approved
clean up
