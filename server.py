from fastapi import FastAPI
from blinkstick_python.blinkstick import blinkstick
import logging
import webcolors

print("__name__ = " + __name__)
logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

bs = blinkstick.find_first()
app = FastAPI(
    title="BlickStick-Square API Server",
    summary="RESTful API server to control the BlinkStick Square",
    version="1.1",
)


def color_to_hex(color):
    return webcolors.name_to_hex(color)


def color_from_hex(hex):
    return webcolors.hex_to_name(hex)


@app.get("/")
def read_root():
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = bs.get_color(color_format="hex")
        name = color_from_hex(hex)
        logger.debug(f'name: {name}, hex: {hex}')
        return {"result": {"name": name, "hex": hex}}
    except Exception as e:
        logger.debug(str(e))
        return {"result": False}


@app.get("/on")
def on(color: str = "green"):
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.set_color(hex=hex)
        logger.debug(f'name: {color}, hex: {hex}')
        return {"result": True}
    except Exception as e:
        logger.debug(str(e))
        return {"result": False}


@app.get("/off")
def off():
    if bs is None:
        return {"error": "no device found"}
    try:
        bs.turn_off()
        logger.debug('turned off')
        return {"result": True}
    except Exception as e:
        logger.debug(str(e))
        return {"result": False}


@app.get("/pulse")
def pulse(
    color: str = "blue",
    duration: int = 1000,
    steps: int = 50
):
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.pulse(hex=hex, duration=duration, steps=steps)
        logger.debug(f"pulsed in {color} for {duration}ms in {steps} steps")
        return {"result": True}
    except Exception as e:
        logger.debug(str(e))
        return {"result": False}


@app.get("/blink")
def blink(
    color: str = "green",
    delay: int = 500,
    repeats: int = 3
):
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.blink(hex=hex, delay=delay, repeats=repeats)
        logger.debug(f"blinked in {color} for {delay}ms {repeats} times")
        return {"result": True}
    except Exception as e:
        logger.debug(str(e))
        return {"result": False}


@app.get("/morph")
def morph(
    color: str = "yellow",
    duration: int = 6000,
    steps: int = 100
):
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.morph(hex=hex, duration=duration, steps=steps)
        logger.debug(f"morphed to {color} in {duration}ms in {steps} steps")
        return {"result": True}
    except Exception as e:
        logger.debug(str(e))
        return {"result": False}
