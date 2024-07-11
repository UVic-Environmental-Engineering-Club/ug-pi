
# No shebang, not executable. Run this with bash directly

# Makes a file somewhere

log_path='/home/pi/Documents/setup.log'

echo $(pwd)

ping -c uveec.ca >> $log_path 2>&1
