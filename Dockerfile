FROM ros:humble
MAINTAINER Philip Esclamado <philipesclamado@uvic.ca>

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y \
    tmux \
    vim \
    python3 \
    python3-pip

RUN useradd --create-home --groups sudo --shell /bin/bash uveec
RUN echo '%sudo ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers

USER uveec
RUN mkdir -p ~/ros2_ws
WORKDIR /home/uveec/ros2_ws/ug-pi

USER root
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip3 install pipenv
RUN pipenv run python -m pip install --upgrade pip
COPY Pipfile .
COPY Pipfile.lock .
RUN pipenv install

CMD ["bash"]
