#!/usr/bin/env pwsh

# The coverage was done due to Python 3 migration
# https://docs.python.org/3/howto/pyporting.html

$SRC="blinkstick-python/blinkstick"

coverage run --debug config --parallel-mode --rcfile=coverage_win32.rc test.py

coverage combine --keep --append --rcfile=coverage_win32.rc .\coverage\

coverage report --show-missing --rcfile=coverage_win32.rc $SRC\*.py

coverage html --rcfile=coverage_win32.rc --no-skip-covered -d coverage/win32

coverage report --show-missing   # vs Other BlickSticks / MacOS