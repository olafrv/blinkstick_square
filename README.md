# BlinkStick Square RESTful API Server

The Unofficial [RESTful API server](server.py) and 
[test](test.py) Python3 scripts to control the
[BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) 
device.

## Pre-Requisites

* A [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) device.
* Data transfer capable cable from Micro USB Male to USB 1.1/2.0/3.0 Male.
* A Python 3.12+ +pip3 working enviroment setup.
* Clone the repository with the following commands:

```sh
git clone https://github.com/olafrv/blinkstick_square
git submodule update --init
pip3 install -r requirements.txt
```

## Usage

### Microsoft Windows Tips 

* Add User's Python Path, <WIN>+R > Run: sysdm.cpl > Environment Variables > System Variables > Path > Edit
* Execute `taskkill /f /im "uvicorn.exe"` or `taskkill /f /im "python.exe"`  to kill any running server

### Testing the RESTful Server

* Start the server with the following command:
```sh
BS_SQ_API_USERNAME="admin"
BS_SQ_API_PASSWORD="strong-password-here"
uvicorn server:app
python server.py  # Alternative
```

* Head to http://localhost:8001/docs API frontend.
* Click on 'Authorize' button and enter the credentials
* Expand the GET methods and click on 'Try it out' option.
* Fill out the parameters and click on 'Execute' button.

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
* UviCorn: https://www.uvicorn.org
