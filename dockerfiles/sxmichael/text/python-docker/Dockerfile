FROM debian:jessie

RUN apt-get update -y && \
    apt-get install --no-install-recommends -y -q build-essential python2.7 python2.7-dev python-pip git && \
    pip install -U pip && \
    rm -rf /var/lib/apt/lists/*
