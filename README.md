# BlinkStick Square RESTful API Server

The Unofficial [RESTful API server](server.py) and 
[test](test.py) Python3 scripts to control the
[BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) 
device.

https://github.com/olafrv/blinkstick_square/assets/987499/0d43afc5-ec32-4dd1-9299-25bf6d0d29a1

## Pre-Requisites

### Basics

* A [BlinkStick Square](https://www.blinkstick.com/products/blinkstick-square) device.
* Data transfer capable cable from Micro USB Male to USB 1.1/2.0/3.0 Male.
* A Python 3.12+ +pip3 working enviroment setup (optionally, virtual).

### Installation

* Clone the repository with the following commands:

```sh
git clone https://github.com/olafrv/blinkstick_square
cd blinkstick_square
git submodule update --init
python -m venv .venv       # if you want to use Python Virtual enviroment
source .venv/bin/activate  # if you want to use Python Virtual enviroment 
pip3 install -r requirements.txt
```

### MacOS Tips

![MacOS USB Devices](./docs/macos_usb_devices.png)

* Install `libusb` with the command `brew install libusb`.
* Use `sudo` to allow USB access when executing `python` or `uvicorn`.
* Check if BlinkStick visible in the following places/ways (if not **replug** it):
  * [System Information > USB](https://support.apple.com/en-gb/guide/mac-help/mchlp1641/mac).
  * Running: `system_profiler SPUSBDataType` or `ioreg -p IOUSB`.
  * Running: My [MacOS utility](./macos_utils/list_devices.sh).
  * Alternatively, [lsusb](https://github.com/jlhonora/lsusb) (A `system_profiler`` wrapper in Bash).

### Microsoft Windows Tips 

* Add User's Python Path, <WIN>+R > Run: sysdm.cpl > Environment Variables > System Variables > Path > Edit
* Execute `taskkill /f /im "uvicorn.exe"` or `taskkill /f /im "python.exe"`  to kill any running server.

### Microsoft WSL2 Tips

* Close (quit) [BlinkStick Client App](https://www.blinkstick.com/help/downloads) as it will block the USB device.
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
sudo udevadm control --reload-rules  # Sometimes reboot is required!
```
* Second, from Windows list and attach the device to the WSL2 Linux:
```sh
# Windows Command Prompt (CMD) as Administrator
C:\Windows\System32>usbipd wsl list
2-2    20a0:41e5  USB Input Device  Not Attached
C:\Windows\System32>usbipd wsl attach --busid=2-2
C:\Windows\System32>usbipd wsl list
2-2    20a0:41e5  USB Input Device  Attached - WSL
```
* Third, inside the WSL2 Linux list the device:
```sh
# WSL2 Linux Shell
$ apt install usbutils
$ lsusb
Bus 001 Device 003: ID 20a0:41e5 Clay Logic BlinkStick
```

### Raspberry Pi + Raspbian OS Tips

* The command `lsusb` should be already installed.
* Add the udev rules (See Microsoft WSL2 Tips) and reboot.
* Then you should see the USB device with `lsusb -vvv` (without errors).

## Usage

### Set Username and Password inside `.env`

```sh	
BS_SQ_API_USERNAME="admin"            # If not set, defaults to "admin"
BS_SQ_API_PASSWORD="strong-password"  # If not set, defaults to RANDOM value!
```

### Option 1: Uvicorn or Python w/wo Python Virtual Environment

* Start the server with one of the following command:
```sh
# See the previous tips sections if facing issues
uvicorn server:app  # default
uvicorn --host 0.0.0.0 --port 8000 server:app
python3 server.py  # alternative without uvicorn
# If Python virtual environment (sudo ignores $PATH):
.venv/bin/uvicorn server:app
.venv/bin/uvicorn server:app --host 0.0.0.0 --port 8000 server:app
.venv/bin/python3 server.py
```

### Option 2: Docker Compose

```sh
docker compose up -d
docker logs blinkstick_square
```

### Run the application on boot

```bash
bash service.sh  # Install the service on boot
journalctl -u blinkstick  # Check the service logs (Also './logs/*.log')
# sudo systemctl stop blinkstick
# sudo systemctl start blinkstick
```

### Access API Frontend

* Go to http://localhost:8000/ (or http://<IP>:8000).
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
* Testing USB Hardware/Drivers on Windows:
  * https://learn.microsoft.com/en-us/windows-hardware/drivers/usbcon/muttutil
  * https://learn.microsoft.com/en-us/windows-hardware/drivers/usbcon/how-to-retrieve-information-about-a-usb-device