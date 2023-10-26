#!/bin/bash

# https://docs.python.org/3/howto/pyporting.html

# MacOS Pre-Requisites

# brew install libusb
# pip3 install pyusb

git clone https://github.com/arvydas/blinkstick-python.git 2>/dev/null

SRC=blinkstick-python/blinkstick

sudo coverage run --rcfile=.coveragerc test.py

coverage report --show-missing $SRC/*.py