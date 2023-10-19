# ug-pi

DIVE: Deep-sea Intelligent Vehicle Exploration

## Docker

- To build the Docker image
  - `docker build -t ug:dev .`
- To run the Docker container and open the shell
  - On Unix: `docker run -it --name ug-pi --rm --volume $(pwd):/home/uveec/ros2_ws/ug-pi ug:dev bash`
  - On Windows: `docker run -it --name ug-pi --rm --volume ${pwd}:/home/uveec/ros2_ws/ug-pi ug:dev bash`
  - Then in the shell use `pipenv shell` to start the python environment

## Maintainers

| Team Member      | Responsibility | Contact                  |
| ---------------- | -------------- | ------------------------ |
| Philip Esclamado | Lead Engineer  | philipesclamado@uvic.ca  |
| David Kim        | Software Lead  | daehwankim@uvic.ca       |
| Rowan Althorp    | Member         | rowalthorp@gmail.com     |
| Anthony Cieri    | Member         | penguinmillion@gmail.com |

## What we used

[<img alt="Docker" src="https://img.shields.io/badge/-RaspberryPi-C51A4A?style=for-the-badge&logo=Raspberry-Pi" />](https://www.raspberrypi.com) [<img alt="Docker" src="https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white" />](https://www.docker.com) [<img alt="ROS.js" src="https://img.shields.io/badge/ros-%230A0FF9.svg?style=for-the-badge&logo=ros&logoColor=white" />](https://www.ros.org) [<img alt="Ubuntu" src="https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white" />](https://ubuntu.com) [<img alt="Python" src="https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54" />](https://www.python.org) [<img alt="Git" src="https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white" />](https://git-scm.com)
