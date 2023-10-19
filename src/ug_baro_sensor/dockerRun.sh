#!/bin/bash

docker build -t ros:dev .

# Don't fuck this up
docker run -itd -v /home/penguin/Documents/Projects/Uveec/DIVE/ug-pi/src/ug_baro_sensor:/home/uveec/ros2_ws/ug-pi ros:dev
# if zsh says
# zsh: correct '/home/penguin/Documents/Projects/Uveec/DIVE/ug-pi/src/ug_baro_sensor:/home/uveec/ros2_ws/ug-pi' to '/home/penguin/Documents/Projects/Uveec/DIVE/ug-pi/src/ug_baro_sensor/home/uveec/ros2_ws/ug-pi' [nyae]?
# Say 'n'

docker exec -it <container name> su uveec

# Then in the terminal
sudo ./env_setup.sh

# then u gotta
reset
# or
exit
docker exec -it <container name> su uveec
# Now everything should be good
