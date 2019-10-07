# catbot.py
# version 0.2.0+

import os

# initial setup. re-use if entire repo blown away
# os.system('git clone https://github.com/joclaire2/catbot')

# clean up local checkout if anyone's been tinkering
# os.system('git reset --hard')

os.chdir('./catbot')
os.system('git status')
os.system('git pull')
os.system('git status')

os.system('python catbot.py')
