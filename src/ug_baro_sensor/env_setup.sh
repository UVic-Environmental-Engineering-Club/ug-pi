#!/bin/bash
# run with sudo

bshrc="/home/uveec/.bashrc"
echo "source /usr/share/colcon_argcomplete/hook/colcon_argcomplete.bash" >> $bshrc

chmod +x /opt/ros/humble/*sh

echo "source /home/penguin/Documents/Projects/Uveec/DIVE/ug-pi/src/ug_baro_sensor/install" >> $bshrc

echo "source /opt/ros/humble/setup.bash" >> $bshrc

chown -R uveec ~/
