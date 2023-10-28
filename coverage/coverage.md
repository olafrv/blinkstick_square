## Python 3 Code Coverage Tests

### BlinkStick Square + MacOS Sonoma 14.0 + MacBook Pro Apple M1 + Python 3.11.6

Output of [coverage.sh](coverage.sh) using [coverage_macm1.rc](coverage_macm1.rc):

```sh
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
blinkstick-python/blinkstick/__init__.py         8      0   100%
blinkstick-python/blinkstick/_version.py         1      0   100%
blinkstick-python/blinkstick/blinkstick.py     219      6    97%   264, 411-412, 452-454, 615
--------------------------------------------------------------------------
TOTAL                                          228      6    97%
```

### BlinkStick Square + Windows 11 23H2 + ASUS-G713RW AMD + Python 3.11.6

Output of [coverage.ps1](coverage.ps1) using [coverage_win32.rc](coverage_win32.rc):

```sh
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
blinkstick-python/blinkstick\__init__.py         8      0   100%
blinkstick-python/blinkstick\_version.py         1      0   100%
blinkstick-python/blinkstick\blinkstick.py     251     44    82%   14-15, 218, 223-224, 238, 243-244, 251-252, 263-268, 288, 300, 371, 411-412, 452-454, 612-617, 820-829, 1555-1558, 1596-1610
--------------------------------------------------------------------------
TOTAL                                          260     44    83%
```
