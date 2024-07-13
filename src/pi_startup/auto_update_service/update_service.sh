
#! /bin/bash

cp auto-update.service /etc/systemd/system/

systemctl reload-daemon
systemctl enable auto-update
