## Git Set up

# 1. identity (your real name — it shows on every commit)
git config --global user.name "Seamus YourLastName"
git config --global user.email "the-email-on-your-github"
git config --global init.defaultBranch main   # so local matches GitHub's "main"

# 2. turn this folder into a local git repo
git init

# 3. a Python .gitignore so junk never gets committed
printf ".venv\n__pycache__/\n*.pyc\n.pytest_cache\n.env\n*.db\n" > .gitignore

# 4. a starter README and your first real commit
echo "# HENNGE Prep" > README.md
git add .
git commit -m "chore: initial commit with gitignore and readme"
