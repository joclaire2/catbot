# catbot main.py
# version 0.2.0+

import os

# os.system('rm -fr ./catbot')

# initial setup. re-use if entire repo blown away
# os.system('git clone https://github.com/joclaire2/catbot')

#os.system('cp ./catbot/main.py ./')
os.chdir('./catbot')

# clean up local checkout if anyone's been tinkering
os.system('git reset --hard')
# softer option to cloning
os.system('git pull origin master')

os.system('python db_setup.py')
# os.system('python db_test.py')

os.system('python catbot.py')
