
#! /bin/bash

cp auto-update.service /etc/systemd/system/

systemd reload-daemon
systemd enable auto-update
