import sys
import logging
from datetime import datetime
from fastapi import FastAPI
import uvicorn
sys.path.append('./blinkstick-python')
from blinkstick import blinkstick  # noqa: E408, E402  # type: ignore

logging.config.fileConfig('logging.conf', disable_existing_loggers=False)

logger = logging.getLogger(__name__)
bs = blinkstick.find_first()
app = FastAPI(
    title="BlickStick-Square API Server",
    summary="RESTful server to control the BlinkStick Square",
    version="1.0",
)

@app.get("/")  # noqa: E302
def read_root():
    hex = bs.get_color(color_format="hex")
    css = [name for name,value in bs._names_to_hex.items() if value == hex]
    if len(css)>0:
        css = css[0] 
    else: 
        css = ''
    logger.info(str(css)) 
    return {
        "css": css,
        "hex": hex
    }

@app.get("/on")
def on(
    css: str = None,
    hex: str = None
):
    success = False
    try:
        bs.set_color(name=css, hex=hex)
        success = True
    except Exception as e:
        logger.info(str(e))
    return {"result": success}

@app.get("/off")
def off():
    success = False
    try:
        bs.turn_off()
        success = True
    except Exception as e:
        logger.info(str(e))
    return {"result": success}


@app.get("/pulse")
def pulse(
    css: str = "green",
    hex: str = "#008000",
    duration: int = 1000,
    steps: int = 50
):
    success = True
    try:
        bs.pulse(name=css, hex=hex, duration=duration, steps=steps)
        logger.info("Pulsed")
        success = True
    except Exception as e:
        logger.info(str(e))
    return {"result": success}

@app.get("/blink")
def blink(
    css: str = "green",
    hex: str = "#008000",
    delay: int = 500,
    repeats: int = 3
):
    success = False
    try:
        bs.blink(name=css, hex=hex, delay=delay, repeats=repeats)
        logger.info(f"blinked for {delay}ms {repeats} times")
        success = True
    except Exception as e:
        logger.info(str(e))
    return {"result": success}

@app.get("/morph")
def morph(
    css: str = "yellow",
    hex: str = "#FFFF00",
    duration: int = 6000,
    steps: int = 100
):
    success = False
    try:
        bs.morph(name=css, hex=hex, duration=duration, steps=steps)
        logger.info(f"morphed to {css} in {duration}ms in {steps} steps")
        success = True
    except Exception as e:
        logger.info(str(e))
    return {"result": success}
