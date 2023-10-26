#!/usr/bin/env pwsh

# The coverage was done due to Python 3 migration
# https://docs.python.org/3/howto/pyporting.html

$SRC="blinkstick-python/blinkstick"

coverage run --debug config --parallel-mode --rcfile=coverage_win32.rc test.py

coverage report --show-missing $SRC\*.py