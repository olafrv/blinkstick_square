# BlinkStick Square

[RESTful API server](server.py) and [test script](test.py) to control the
[BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square).

## Pre-Requisites

* A [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) device.
* Data transfer capable cable from Micro USB Male to USB 1.1/2.0/3.0 Male.
* A working Python 3.12+ with pip3 enviroment setup.
* Finally, run the following commands:

```sh
git clone https://github.com/olafrv/blinkstick_square
git submodule update --init --recursive
pip3 install -r requirements.txt
```

## RESTful Server

```sh
# Microsoft Windows Tips: 
# Add User's Python Binary Path, <WIN>+R > Run: sysdm.cpl
# > Environment Variables > System Variables > Path > Edit
# taskkill /f /im "uvicorn.exe"  # Kill any running server
uvicorn server:app  # --reload
```

Head to http://localhost:8001/docs#/ API frontend.
Use 'Try it out' option on the GET methods.

## Test & Coverage

See [coverage.md](coverage.md) for details of environment
and the lastest tests coverage.

```sh
# As root / Administrator to allow USB access
python3 test.py               # Tests
sh coverage/coverage.sh       # Coverage Unix-Like
pwsh coverage\coverage.ps1    # Coverage Windows
```

The output of the test/coverage is as follows:

```sh
Python Package: 1.2.0
Serial:         BS******-*.*
Variant:        BlinkStick Square
Manufacturer:   Agile Innovative Ltd
Description:    BlinkStick
Info Block 1:   Olaf Retmaier
Info Block 2:   olafrv@gmail.com
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

## Todos

* WSL2 USB Tests
  * https://gitlab.com/alelec/wsl-usb-gui
  * https://github.com/dorssel/usbipd-win

## References

* BlinkStick: https://www.blinkstick.com
* Unix-Like: https://github.com/pyusb/pyusb
* Windows: https://pypi.org/project/pywinusb
* SRC: https://github.com/arvydas/blinkstick-python
* API: https://arvydas.github.io/blinkstick-python/
* Coverage: https://coverage.readthedocs.io/en/7.3.2/
* FastAPI: https://fastapi.tiangolo.com
