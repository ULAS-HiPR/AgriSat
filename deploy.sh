#!/bin/bash -e

sudo cp AgriSat.service /etc/systemd/system/AgriSat.service
sudo systemctl daemon-reload
sudo systemctl enable AgriSat.service
sudo systemctl start AgriSat.service