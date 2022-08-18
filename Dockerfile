FROM ubuntu:20.04

ENV DEBIAN_FRONTEND noninteractive

SHELL ["/bin/bash", "-c"]

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y python3-pip python-xlib python3-xlib && \
    apt-get install -y python3.8-venv && \
    apt-get install -y net-tools iputils-ping

# create python3 VENV
ENV VIRTUAL_ENV=~/venv/py3
RUN python3 -m venv --system-site-packages $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"
RUN pip install --upgrade pip setuptools wheel numpy scipy

COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .

WORKDIR /src
CMD ["python3"]
