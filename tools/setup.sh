#!/bin/sh

python3 -m venv env
. ./env/bin/activate
pip3 install --upgrade pip
pip3 install -r requirements.txt
deactivate
