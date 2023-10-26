# Python 3 Code Coverage Tests

## BlinkStick Square + MacOS Sonoma 14.0 + MacBook Pro Apple M1 + Python 3.11.6

### Coverage Command

See [coverage.sh](coverage.sh)

### Coverage Percentage

```sh
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
blinkstick-python/blinkstick/__init__.py         8      0   100%
blinkstick-python/blinkstick/_version.py         1      0   100%
blinkstick-python/blinkstick/blinkstick.py     219      8    96%   264, 411-412, 452-454, 615, 824-825
--------------------------------------------------------------------------
TOTAL                                          228      8    96%
```

## BlinkStick Square + Windows 11 23H2 + ASUS-G713RW AMD + Python 3.11.6

```sh
Name                                         Stmts   Miss  Cover   Missing
--------------------------------------------------------------------------
blinkstick-python\blinkstick\__init__.py         8      0   100%
blinkstick-python\blinkstick\_version.py         1      0   100%
blinkstick-python\blinkstick\blinkstick.py     219     38    83%   14-15, 218, 223-224, 251-252, 263-268, 288, 300, 371, 411-412, 452-454, 612-617, 820-829, 1558, 1596-1610
test.py                                         84      1    99%   39
--------------------------------------------------------------------------
TOTAL                                          312     39    88%
```

### Coverage Lines Ignored

See [.coveragerc](.coveragerc) for safely ignored lines and the reasons.
