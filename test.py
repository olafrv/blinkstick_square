#!/usr/bin/env python3

import sys
from time import sleep

sys.path.append('./blinkstick-python')

from blinkstick import blinkstick  # noqa: E408, E402  # type: ignore

print("Package Version: " + blinkstick.get_blinkstick_package_version())

for bstick in blinkstick.find_all():
    print("Serial:        " + bstick.get_serial())
    print("Variant:       " + bstick.get_variant_string())
    print("Manufacturer:  " + bstick.get_manufacturer())
    print("Description:   " + bstick.get_description())

    # See .coveragerc for details
    # print("Setting Info Block 1")
    # bstick.set_info_block1("Olaf Reitmaier")
    info1 = bstick.get_info_block1()
    print("Info Block 1:  " + info1)

    # See .coveragerc for details
    # print("Setting Info Block 2")
    # bstick.set_info_block2("olafrv@gmail.com")
    info2 = bstick.get_info_block2()
    print("Info Block 2:  " + info2)

bstick = None

print("---")
print("Finding first device...")
led = blinkstick.find_first()

if led:

    print("LEDs Count: " + str(led.get_led_count()))  # -1 <=> Unsupported

    print("---")
    print("Turning on 🟥 RED...")
    led.set_error_reporting(False)
    led.set_color(hex="#f00")  # name="red" , expands to hex="#ff0000"
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(3)

    print("---")
    print("Turning on 🟧 ORANGE...")
    led.set_error_reporting(True)
    led.set_color(name="orange")
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(3)

    print("---")
    print("Turning on 🟥 RED? (Max RGB Value=128) ...")
    led.get_max_rgb_value(None)  # This function must be fixed
    led.set_max_rgb_value(128)
    led.set_color(red=255, green=0, blue=0)  # name="red"
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(3)
    led.set_max_rgb_value(255)
    led.get_max_rgb_value(None)

    print("---")
    print("Inverse of ⬛ BLACK is ⬜ WHITE ...")
    led.get_inverse()
    led.set_inverse(True)
    led.set_color(name="black")
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(3)
    led.set_inverse(False)

    print("---")
    print("Pulsing on 🟦 BLUE...")
    led.pulse(name="blue", duration=1000, repeats=3)
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(1)

    print("---")
    print("Blinking on 🟩 GREEN...")
    led.blink(name="green", delay=1000, repeats=3)
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(3)

    print("---")
    print("Morphing from 🟦 GREEN => 🟨 YELLOW ...")
    led.set_color(name="blue")
    led.morph(name="yellow", duration=6000, steps=100)
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(3)

    print("---")
    print("Random 2x🎁 COLORS ...")
    led.set_color(name="random")
    sleep(3)
    led.set_random_color()
    print("Color: " + led.get_color(color_format="hex"))
    print("Color: " + str(led.get_color(color_format="rgb")))
    sleep(3)

    print("Turning ⬇️ OFF")
    led.turn_off()

led = None
