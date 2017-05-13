FROM ubuntu:16.04
LABEL name=docker-data-science version=latest

MAINTAINER ASI Data Science <engineering@asidatascience.com>

ADD ["requirements-conda.txt", "requirements-pip.txt", "/"]

ENV MINICONDA_VERSION 4.1.11
ENV PATH /opt/miniconda/bin:${PATH}

RUN apt-get update -qq && \
    env DEBIAN_FRONTEND=noninteractive apt-get install -qq \
    bzip2 curl libglib2.0-0 libxext6 libsm6 libxrender1 && \
    curl -sLO https://repo.continuum.io/miniconda/Miniconda2-$MINICONDA_VERSION-Linux-x86_64.sh && \
    echo "a9714094c73e4593849438d82ed4dd7374d3466decd4d6c92871758b313d78ce00b653e40038e0b5295e794a068dbd7a12c5e600e28abec67d8715155a74ba5f Miniconda2-$MINICONDA_VERSION-Linux-x86_64.sh" | sha512sum -c && \
    bash Miniconda2-$MINICONDA_VERSION-Linux-x86_64.sh -p /opt/miniconda -b && \
    rm Miniconda2-$MINICONDA_VERSION-Linux-x86_64.sh && \
    conda update -qy conda && \
    # Prevent MKL optimisations being installed (require licence after 30 days).
    conda install -qy nomkl && \
    conda install -qy --file /requirements-conda.txt && \
    rm /requirements-conda.txt && \
    pip install -qr /requirements-pip.txt && \
    rm /requirements-pip.txt && \
    # Clean apt, pip, and conda caches to reduce image size.
    apt-get clean && \
    rm -fr /var/lib/apt/lists/* /root/.cache/pip && \
    conda clean -y --all

VOLUME /var/jupyter

WORKDIR /var/jupyter

EXPOSE 8888
CMD env SHELL=/bin/bash jupyter notebook --ip=0.0.0.0 --no-browser --port=8888
