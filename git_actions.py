import os

os.system('git status')
# os.system('git remote -v')

# os.system('git checkout development')
# os.system('git checkout master')

# clean up local checkout if anyone's been tinkering
#os.system('git reset --hard')

# softer option to cloning
os.system('git pull origin master')

os.system('git config --global user.email "ribman@gmail.com"')

os.system('git config --global user.name "Rob Manthey"')

os.system('git add *')

os.system('git commit -m "Setting up push from Repl.it"')

os.system('git push --set-upstream origin master')

os.system('git status')
