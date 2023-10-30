FROM ubuntu:22.04 as base
RUN apt update -y \
    && apt install -y tzdata \
    && apt install -y python3 \
    && apt install -y python3.10-venv\
    && apt install -y --no-install-recommends build-essential gcc \
    && apt install -y usbutils \
    && apt clean

FROM base 

# This is required to autolink the package to the repository in github
LABEL org.opencontainers.image.source=https://github.com/olafrv/blinkstick_square
LABEL org.opencontainers.image.description="BlinkStick Square RESTful API Server"
LABEL org.opencontainers.image.licenses=MIT

WORKDIR /opt/blinkstick_square
COPY requirements.txt /opt/blinkstick_square/
COPY blinkstick_python /opt/blinkstick_square/blinkstick_python
COPY server.py /opt/blinkstick_square/

ENV PYTHONUNBUFFERED 1
RUN python3 -m venv /opt/venv
ENV PATH="/opt/venv/bin:$PATH"
RUN pip3 install -Ur requirements.txt \
    && pip install --upgrade pip

ENTRYPOINT [ "python3" , "server.py" ]
CMD [ "-c" ]