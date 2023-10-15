#!/bin/bash

# bash script for ci/cd


sudo apt update
sudo apt upgrade -y
sudo rm -rf movies
sudo mkdir ~/movies
cd ~/movies
sudo apt install python3 -y
sudo apt install python3-pip -y
sudo python3 -m venv venv
sudo apt install git -y
sudo git clone https://github.com/bluelambdatech/movies-point.git
cd movies-point
sudo git checkout dev
sudo cp /project/movies-point/.env ~/movies/movies-point
sudo virtualenv venv
source venv/bin/activate
sudo pip3 install -r requirements.txt
sudo uvicorn main:app --host 0.0.0.0 --port 80


