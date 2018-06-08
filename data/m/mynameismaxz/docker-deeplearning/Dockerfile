FROM nvidia/cuda:8.0-cudnn5-devel-ubuntu14.04  
MAINTAINER Sirachat Sirilert <sirachat.siri@mail.kmutt.ac.th>  
  
ARG TENSORFLOW_VERSION=1.2.1  
ARG TENSORFLOW_ARCH=gpu  
  
# Pick up some TF dependencies  
# Install requirement package for c9  
RUN apt-get update && apt-get install -y --no-install-recommends \  
build-essential \  
g++ \  
libssl-dev \  
apache2-utils \  
git \  
libxml2-dev \  
sshfs \  
curl \  
libfreetype6-dev \  
libpng12-dev \  
libzmq3-dev \  
pkg-config \  
python3 \  
python3-dev \  
python3-tk \  
python \  
python-dev \  
rsync \  
software-properties-common \  
unzip  
  
# Install Supervisor  
RUN apt-get install -y supervisor && \  
sed -i 's/^\\(\\[supervisord\\]\\)$/\1\nnodaemon=true/'
/etc/supervisor/supervisord.conf  
  
# Define mountable directories.  
VOLUME ["/etc/supervisor/conf.d"]  
  
#
------------------------------------------------------------------------------  
# Security changes  
# - Determine runlevel and services at startup [BOOT-5180]  
RUN update-rc.d supervisor defaults  
  
# Define working directory.  
WORKDIR /etc/supervisor/conf.d  
#
------------------------------------------------------------------------------  
# Install pip3 for python  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && \  
python3 get-pip.py && \  
rm get-pip.py  
  
# Install requirement package for deeplearning  
RUN pip3 --no-cache-dir install \  
ipykernel \  
jupyter \  
matplotlib \  
numpy \  
scipy \  
sklearn \  
keras \  
pandas \  
Pillow \  
&& \  
python3 -m ipykernel.kernelspec  
  
# Install TensorFlow GPU version.  
RUN pip --no-cache-dir install \  
https://storage.googleapis.com/tensorflow/linux/gpu/tensorflow_${TENSORFLOW_ARCH}-${TENSORFLOW_VERSION}-cp34-cp34m-linux_x86_64.whl  
  
# ------------------------------- C9 Section -------------------------------  
RUN curl -sL https://deb.nodesource.com/setup | bash -  
RUN apt-get install -y nodejs  
  
# Install Cloud9  
RUN git clone https://github.com/c9/core.git /cloud9  
WORKDIR /cloud9  
RUN scripts/install-sdk.sh  
  
# Set up our notebook config.  
COPY config/jupyter_notebook_config.py /root/.jupyter/  
  
# For CUDA profiling, TensorFlow requires CUPTI.  
ENV LD_LIBRARY_PATH /usr/local/cuda/extras/CUPTI/lib64:$LD_LIBRARY_PATH  
  
# Tweak standlone.js conf  
RUN sed -i -e 's_127.0.0.1_0.0.0.0_g' /cloud9/configs/standalone.js  
  
# Add supervisord conf  
ADD config/cloud9.conf /etc/supervisor/conf.d/  
ADD config/jupyter.conf /etc/supervisor/conf.d/  
  
# Add volumes  
RUN mkdir /workspace  
VOLUME /workspace  
  
# Clean up APT when done.  
RUN apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/*  
  
# TensorBoard  
EXPOSE 6006  
# IPython  
EXPOSE 8888  
# Cloud9  
EXPOSE 80  
EXPOSE 3000  
WORKDIR "/workspace"  
  
CMD ["supervisord", "-c", "/etc/supervisor/supervisord.conf"]

