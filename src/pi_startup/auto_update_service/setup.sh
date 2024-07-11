
# No shebang, not executable. Run this with bash directly

# Test script
# Runs some other scripts

git_dir='/home/pi/Documents/ug-pi/'

cd git_dir

git pull >> ~/Documents/setup.log

echo $(pwd) > testing.txt

bash ./src/pi_startup/startup_stuff/test.sh

python3 ./src/pi_startup/startup_stuff/test.py > ~/Documents/test_py_output.txt
