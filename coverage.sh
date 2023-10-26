#!/bin/bash

# The coverage was done due to Python 3 migration
# https://docs.python.org/3/howto/pyporting.html

SRC="blinkstick-python/blinkstick"

sudo coverage run --debug config --parallel-mode --rcfile=coverage_macm1.rc test.py

coverage report --show-missing $SRC/*.py