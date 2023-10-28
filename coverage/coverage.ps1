#!/usr/bin/env pwsh

$SRC="blinkstick-python\blinkstick"
$RCFILE="coverage\coverage_win32.rc"

coverage run --debug config --parallel-mode --rcfile=$RCFILE test.py
coverage combine --keep --append --rcfile=$RCFILE .\coverage\
coverage report --show-missing --rcfile=$RCFILE $SRC\*.py
coverage html --rcfile=$RCFILE --no-skip-covered -d coverage/htmlcov_win32
coverage report --show-missing   # vs Other BlickSticks / MacOS