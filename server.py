import os
import time
import logging
import webcolors
import secrets
import uvicorn
from typing import Annotated
from fastapi import FastAPI, Request, Depends, HTTPException, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import HTTPBasic, HTTPBasicCredentials
from fastapi.responses import (
    RedirectResponse,
)
from blinkstick_python.blinkstick import blinkstick
import colorlog


class ColoredFormatter(colorlog.ColoredFormatter):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.converter = time.gmtime


logging.config.fileConfig('logging.conf', disable_existing_loggers=False)
logger = logging.getLogger(__name__)

bs = blinkstick.find_first()
app = FastAPI(
    title="BlickStick-Square API Server",
    summary="RESTful API server to control the BlinkStick Square",
    version="1.1",
    redoc_url=None
)

default_username = os.getenv("BS_SQ_API_USERNAME") or "admin"
default_username_bytes = default_username.encode("UTF-8")
default_password = os.getenv("BS_SQ_API_PASSWORD") or secrets.token_hex(16)
default_password_bytes = default_password.encode("UTF-8")
security = HTTPBasic()


def check_login(
    credentials: Annotated[HTTPBasicCredentials, Depends(security)]
):
    current_username_bytes = credentials.username.encode("utf8")
    is_correct_username = secrets.compare_digest(
        current_username_bytes, default_username_bytes
    )
    current_password_bytes = credentials.password.encode("utf8")
    is_correct_password = secrets.compare_digest(
        current_password_bytes, default_password_bytes
    )
    if is_correct_username and is_correct_password:
        logging.info(f"user '{credentials.username}' authenticated")
        return credentials.username
    else:
        logging.error(f"user '{credentials.username}' authentication failed")
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )


app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:8000",
        "*"
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.middleware("http")
async def add_process_time_header(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time
    response.headers["X-Process-Time"] = str(process_time)
    return response


def color_to_hex(color):
    return webcolors.name_to_hex(color)


def color_from_hex(hex):
    return webcolors.hex_to_name(hex)


@app.get("/")
def root():
    response = RedirectResponse(url='/docs#')
    return response


@app.get("/color")
def color(
    username: Annotated[HTTPBasicCredentials, Depends(check_login)] = None
):
    if username is None:
        return {"error": "not authenticated"}
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = bs.get_color(color_format="hex")
        name = color_from_hex(hex)
        logger.info(f'name: {name}, hex: {hex}')
        return {"result": {"name": name, "hex": hex}}
    except Exception as e:
        logger.error(str(e))
        return {"result": False}


@app.get("/on")
def on(
    color: Annotated[str, "HTML Color"] = "green",
    username: Annotated[HTTPBasicCredentials, Depends(check_login)] = None
):
    if username is None:
        return {"error": "not authenticated"}
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.set_color(hex=hex)
        logger.info(f'name: {color}, hex: {hex}')
        return {"result": True}
    except Exception as e:
        logger.error(str(e))
        return {"result": False}


@app.get("/off")
def off(
    username: Annotated[HTTPBasicCredentials, Depends(check_login)] = None
):
    if username is None:
        return {"error": "not authenticated"}
    if bs is None:
        return {"error": "no device found"}
    try:
        bs.turn_off()
        logger.debug('turned off')
        return {"result": True}
    except Exception as e:
        logger.error(str(e))
        return {"result": False}


@app.get("/pulse")
def pulse(
    color: str = "blue",
    duration: int = 1000,
    steps: int = 50,
    username: Annotated[HTTPBasicCredentials, Depends(check_login)] = None
):
    if username is None:
        return {"error": "not authenticated"}
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.pulse(hex=hex, duration=duration, steps=steps)
        logger.info(f"pulsed in {color} for {duration}ms in {steps} steps")
        return {"result": True}
    except Exception as e:
        logger.error(str(e))
        return {"result": False}


@app.get("/blink")
def blink(
    color: str = "green",
    delay: int = 500,
    repeats: int = 3,
    username: Annotated[HTTPBasicCredentials, Depends(check_login)] = None
):
    if username is None:
        return {"error": "not authenticated"}
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.blink(hex=hex, delay=delay, repeats=repeats)
        logger.info(f"blinked in {color} for {delay}ms {repeats} times")
        return {"result": True}
    except Exception as e:
        logger.error(str(e))
        return {"result": False}


@app.get("/morph")
def morph(
    color: str = "yellow",
    duration: int = 6000,
    steps: int = 100,
    username: Annotated[HTTPBasicCredentials, Depends(check_login)] = None
):
    if username is None:
        return {"error": "not authenticated"}
    if bs is None:
        return {"error": "no device found"}
    try:
        hex = color_to_hex(color)
        bs.morph(hex=hex, duration=duration, steps=steps)
        logger.info(f"morphed to {color} in {duration}ms in {steps} steps")
        return {"result": True}
    except Exception as e:
        logger.error(str(e))
        return {"result": False}


if __name__ == "__main__":
    uvicorn.run(app,
                host="0.0.0.0",
                port=8000,
                log_config="logging.conf",
                use_colors=False)
