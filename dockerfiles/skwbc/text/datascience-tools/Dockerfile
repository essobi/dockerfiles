FROM ubuntu:16.04
MAINTAINER Shota Kawabuchi <shota.kawabuchi+github@gmail.com>

RUN set -x && \
  apt-get update && \
  apt-get install -y \
    build-essential \
    libatlas-base-dev \
    libopencv-dev \
    wget \
    git \
    vim \
    libgtk2.0 && \
  apt-get clean && \
  wget https://repo.continuum.io/archive/Anaconda3-4.1.1-Linux-x86_64.sh && \
  bash Anaconda3-4.1.1-Linux-x86_64.sh -b && \
  rm Anaconda3-4.1.1-Linux-x86_64.sh

ENV PATH /root/anaconda3/bin:$PATH
RUN set -x && \
  conda install -c https://conda.binstar.org/menpo opencv3 -y && \
  conda install -c conda-forge tensorflow -y && \
  conda install jupyter -y && \
  conda install seaborn -y && \
  conda install -c conda-forge pymc3 -y && \
  conda install -c conda-forge librosa -y && \
  pip install \
    line_profiler \
    memory_profiler \
    keras

# xgboost
RUN set -x && \
  git clone --recursive https://github.com/dmlc/xgboost && \
  cd xgboost; make -j4 && \
  cd python-package; python setup.py install

# mxnet
ENV MXNET_HOME /mxnet
RUN set -x && \
  git clone https://github.com/dmlc/mxnet.git --recursive && \
  cd /mxnet; make -j4 && \
  cd python; python setup.py install

COPY jupyter_notebook_config.py /root/.jupyter/
COPY matplotlibrc /root/.config/matplotlib/

# TensorBoard
EXPOSE 6006
# Jupyter Notebook
EXPOSE 8888
RUN mkdir /workspace
VOLUME /workspace
VOLUME /mnt
WORKDIR /workspace

