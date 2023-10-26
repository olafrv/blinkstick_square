# BlinkStick Square Tests

A test Python 3 script for the [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) device.

## Pre-Requisites

```bash
brew install libusb     # MacOS
pip3 install pyusb      # Unix-Like Only
pip3 install pywinusb   # Windows Only
pip3 install coverage   # Only for Coverage
python3 tests.py  # as root / administrator
bash coverage.sh  # as root / administrator
```

## References

* BlinkStick: https://www.blinkstick.com
* Unix-Like: https://github.com/pyusb/pyusb
* Windows: https://pypi.org/project/pywinusb
* SRC: https://github.com/arvydas/blinkstick-python
* API: https://arvydas.github.io/blinkstick-python/
* Coverage: https://coverage.readthedocs.io/en/7.3.2/
