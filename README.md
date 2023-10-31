# BlinkStick Square RESTful API Server

The Unofficial [RESTful API server](server.py) and 
[test](test.py) Python3 scripts to control the
[BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) 
device.

https://github.com/olafrv/blinkstick_square/raw/master/docs/BlinkStickSquare480px.mp4


## Pre-Requisites

### Basics

* A [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) device.
* Data transfer capable cable from Micro USB Male to USB 1.1/2.0/3.0 Male.
* A Python 3.12+ +pip3 working enviroment setup.
* Clone the repository with the following commands:

```sh
git clone https://github.com/olafrv/blinkstick_square
git submodule update --init
pip3 install -r requirements.txt
```

### MacOS Tips

* Install `libusb` with the command `brew install libusb`.
* Use `sudo` to allow USB access when executing `python` or `uvicorn`.

### Microsoft Windows Tips 

* Add User's Python Path, <WIN>+R > Run: sysdm.cpl > Environment Variables > System Variables > Path > Edit
* Execute `taskkill /f /im "uvicorn.exe"` or `taskkill /f /im "python.exe"`  to kill any running server.

### Microsoft WSL2 Tips

* Close (quit) BlinkStick Client App as it will block the USB device.
* Follow the instructions to install [usbipd-win](https://github.com/dorssel/usbipd-win)
  described by Microsoft [here](https://learn.microsoft.com/en-us/windows/wsl/connect-usb).
* First, inside your WSL2 Linux:
```sh
sudo apt install linux-tools-generic hwdata
sudo update-alternatives --install /usr/local/bin/usbip usbip /usr/lib/linux-tools/*-generic/usbip 20
cat - | sudo tee /etc/udev/rules.d/99-blinkstick.rules <<EOF
# BlinkStick Square - Allow user to read or write to the device
SUBSYSTEM=="usb", ATTRS{idVendor}=="20a0", ATTRS{idProduct}=="41e5", MODE="0666"
EOF
sudo udevadm control --reload-rules
```
* Second, list and attach the device to the WSL2 Linux:
```sh
# Windows Command Prompt (CMD) as Administrator
C:\Windows\System32>usbipd wsl list
2-2    20a0:41e5  USB Input Device  Not Attached
C:\Windows\System32>usbipd wsl attach --busid=2-2
C:\Windows\System32>usbipd wsl list
2-2    20a0:41e5  USB Input Device  Attached - WSL
```
* Third, list the device inside the WSL2 Linux:
```sh
# WSL2 Linux Shell
$ lsusb
Bus 001 Device 003: ID 20a0:41e5 Clay Logic BlinkStick
```

## Usage

### Set Username and Password

```sh	
export BS_SQ_API_USERNAME="admin"  # If not set, defaults to "admin"
export BS_SQ_API_PASSWORD="strong-password"  # If not set, defaults to random value
```

### Docker Compose

```sh
docker compose up -d
docker logs blinkstick_square
```

### Uvicorn or Python

* Start the server with the following command:
```sh
uvicorn server:app
python server.py    # Alternative
```

### API Frontend

* Head to http://localhost:8000/ API frontend.
* Click on 'Authorize' button and enter the credentials
* Expand the GET methods and click on 'Try it out' option.
* Fill out the parameters and click on 'Execute' button.

## Test & Coverage

See [coverage.md](coverage.md) for details of environment
and the lastest tests coverage.

```sh
python3 test.py               # Tests
sh coverage/coverage.sh       # Coverage Unix-Like
pwsh coverage\coverage.ps1    # Coverage Windows
```

The output of the test/coverage is shown below ([source](docs/bssq_test.cast)):

[![asciicast](https://asciinema.org/a/618281.png)](https://asciinema.org/a/618281) 


## Todos

* Figure out udev rules on MacOS to avoid admin rights.

## References

* BlinkStick: https://www.blinkstick.com
* Unix-Like: https://github.com/pyusb/pyusb
* Windows: https://pypi.org/project/pywinusb
* SRC: https://github.com/arvydas/blinkstick-python
* API: https://arvydas.github.io/blinkstick-python/
* Coverage: https://coverage.readthedocs.io/en/7.3.2/
* FastAPI: https://fastapi.tiangolo.com
* UviCorn: https://www.uvicorn.org
* WLS2 Connect USB Devices:
  * https://learn.microsoft.com/en-us/windows/wsl/connect-usb
  * https://github.com/dorssel/usbipd-win