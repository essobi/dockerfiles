FROM debian:wheezy

MAINTAINER Ozzy Johnson <docker@ozzy.io>

ENV DEBIAN_FRONTEND noninteractive

ENV PYTHON_VERSION 2.7
# Update and install minimal.
RUN \
    apt-get update \
        --quiet \
    && apt-get install \
        --yes \
        --no-install-recommends \
        --no-install-suggests \
    build-essential \
    python$PYTHON_VERSION \
    python$PYTHON_VERSION-dev \
    python-pip \
# Clean up packages.
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Update pip and set up virtualenv.
RUN pip install \
    -U pip

RUN pip install \
    virtualenv

# Default command.
CMD ["bash"]
