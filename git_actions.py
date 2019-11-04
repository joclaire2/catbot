import os

os.system('git status')
# os.system('git remote -v')

# os.system('git checkout development')
# os.system('git checkout master')

<<<<<<< HEAD
os.system('git pull origin master')

os.system('git config --global user.email "ribman@gmail.com"')
=======
# clean up local checkout if anyone's been tinkering
#os.system('git reset --hard')

# softer option to cloning
os.system('git pull origin master')

os.system('git config --global user.email "ribman@gmail.com"')

>>>>>>> b8495a136f7fb36742bac7d6e7df0b2dd822686c
os.system('git config --global user.name "Rob Manthey"')

os.system('git add *')

<<<<<<< HEAD
os.system('git commit -m "working date diff in daily"')
=======
os.system('git commit -m "Setting up push from Repl.it"')
>>>>>>> b8495a136f7fb36742bac7d6e7df0b2dd822686c

os.system('git push --set-upstream origin master')

os.system('git status')
