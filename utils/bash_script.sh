#!/bin/bash

# bash script for ci/cd


sudo apt update
sudo apt upgrade -y
 mkdir movies
sudo apt install python
python install pip
sudo apt install pip
sudo apt install python-pip
sudo pip install virtualenv
mkdir -p movies/source
 cd movies
virtualenv env
sudo apt install git -y
git clone https://github.com/bluelambdatech/movies-point.git
cd movies-point/
source env/bin/activate
git checkout dev
sudo pip install -r requirements.txt 
uvicorn main:app --host 0.0.0.0 --port 80


