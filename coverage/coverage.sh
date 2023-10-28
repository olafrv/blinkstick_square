#!/bin/sh

SRC="blinkstick-python/blinkstick"
RCFILE=coverage_macm1.rc

sudo coverage run --debug config --parallel-mode --rcfile=$RCFILE test.py
coverage combine --keep --append --rcfile=$RCFILE ./coverage
coverage report --show-missing --rcfile=$RCFILE $SRC/*.py
coverage html --rcfile=$RCFILE --no-skip-covered -d coverage/htmlcov_macm1
coverage report --show-missing   # vs Other BlickSticks / Windows
