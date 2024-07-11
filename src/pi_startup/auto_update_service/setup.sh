
# No shebang, not executable. Run this with bash directly

# Test script
# Runs some other scripts

git_dir='/home/pi/Documents/ug-pi'
log_path='/home/pi/Documents/setup.log'

cd $git_dir

touch $log_path
# New line
echo >> $log_path
date >> $log_path

# Send both stdout and stderr to the log
git pull >> $log_path 2>&1

bash $git_dir/src/pi_startup/startup_stuff/test.sh

python3 $git_dir/src/pi_startup/startup_stuff/test.py > ~/Documents/test_py_output.txt
