#!/bin/sh
brew install libusb
incpath=$(find /usr/local -name libusb.h | xargs dirname)
libpath=$(find /usr/local -name libusb-1.0.dylib | xargs dirname)
outfile=list_devices_$(uname -s)_$(uname -m)
echo $incpath
echo $libpath
gcc -I $incpath -L $libpath -o $outfile list_devices.c -lusb-1.0
chmod +x $outfile
./$outfile