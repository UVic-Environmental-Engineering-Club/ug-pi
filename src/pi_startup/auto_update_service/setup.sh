
# No shebang, not executable. Run this with bash directly

# Test script
# Runs some other scripts

git_dir='/home/pi/Documents/ug-pi'
log_path='~/Documents/setup.log'

cd $git_dir

# New line
echo >> $log_path
date >> $log_path

git pull >> $log_path

echo $(pwd) > testing.txt

bash $git_dir/src/pi_startup/startup_stuff/test.sh

python3 $git_dir/src/pi_startup/startup_stuff/test.py > ~/Documents/test_py_output.txt
