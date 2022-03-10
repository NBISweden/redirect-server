#!/bin/sh

# clone git repo
cd / ; git clone https://github.com/NBISweden/redirect-server.git ; cd redirect-server

# start the server
python3 server.py

