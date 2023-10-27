#!/bin/sh

# The coverage was done due to Python 3 migration
# https://docs.python.org/3/howto/pyporting.html

SRC="blinkstick-python/blinkstick"

sudo coverage run --debug config --parallel-mode --rcfile=coverage_macm1.rc test.py

coverage combine --keep ./coverage

coverage report --show-missing --rcfile=coverage_macm1.rc $SRC/*.py

coverage html --rcfile=coverage_macm1.rc --no-skip-covered  # Passed

coverage report --show-missing   # vs Other BlickSticks / Windows