import os

os.system('git status')
# os.system('git remote -v')

# os.system('git checkout development')
# os.system('git checkout master')

os.system('git pull origin master')

os.system('git config --global user.email "ribman@gmail.com"')
os.system('git config --global user.name "Rob Manthey"')

os.system('git add *')

os.system('git commit -m "working date diff in daily"')

os.system('git push --set-upstream origin master')

os.system('git status')
