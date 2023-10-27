# BlinkStick Square Tests

A Python 3 script to test the [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) device.

## Pre-Requisites

A Micro USB Male to Any USB 1.1/2.0/3.0 Female **data transfer** cable (Power only won't work).

```bash
brew install libusb     # MacOS
pip3 install pyusb      # Unix-Like Only
pip3 install pywinusb   # Windows Only
pip3 install coverage   # Only for Coverage
```

## Test

See [coverage.md](coverage.md) for details of the test environment I used.

```bash
git clone https://github.com/olafrv/blinkstick_square
git clone submodule update 
# Run as root / Administrator to allow USB access
python3 tests.py
sh coverage.sh     # Unix-Like
pwsh coverage.ps1  # Windows
```

## Output

```bash
Package Version: 1.2.0
Serial:        BS056011-3.0
Variant:       BlinkStick Square
Manufacturer:  Agile Innovative Ltd
Description:   BlinkStick
Info Block 1:  Olaf Retmaier
Info Block 2:  olafrv@gmail.com
---
Finding first device...
LEDs Count: -1
---
Turning on 🟥 RED...
Color: #ff0000
Color: [255, 0, 0]
---
Turning on 🟧 ORANGE...
Color: #ffa500
Color: [255, 165, 0]
---
Turning on 🟥 RED? (Max RGB Value=128) ...
Color: #800000
Color: [128, 0, 0]
---
Inverse of ⬛ BLACK is ⬜ WHITE ...
Color: #000000
Color: [0, 0, 0]
---
Pulsing on 🟦 BLUE...
Color: #000000
Color: [0, 0, 0]
---
Blinking on 🟩 GREEN...
Color: #000000
Color: [0, 0, 0]
---
Morphing from 🟦 GREEN => 🟨 YELLOW ...
Color: #ffff00
Color: [255, 255, 0]
---
Random 2x🎁 COLORS ...
Color: #d7cfdd
Color: [215, 207, 221]
Turning ⬇️ OFF
```

## References

* BlinkStick: https://www.blinkstick.com
* Unix-Like: https://github.com/pyusb/pyusb
* Windows: https://pypi.org/project/pywinusb
* SRC: https://github.com/arvydas/blinkstick-python
* API: https://arvydas.github.io/blinkstick-python/
* Coverage: https://coverage.readthedocs.io/en/7.3.2/
