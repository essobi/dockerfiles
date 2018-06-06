FROM nvidia/cuda:8.0-cudnn7-devel  
MAINTAINER Yasuyuki YAMADA <yasuyuki.ymd@gmail.com>  
  
RUN apt-get update -y && \  
apt-get install -y --no-install-recommends \  
python3-dev \  
python3-pip \  
python3-wheel \  
python3-setuptools \  
python3 \  
curl \  
git \  
&& \  
rm -rf /var/lib/apt/lists/* /var/cache/apt/archives/*  
  
RUN pip3 install cupy==4.0.0 chainer==4.0.0 matplotlib Pillow
git+https://github.com/yasuyuky/chainer-ya-utils  
RUN mkdir /work  
WORKDIR /work  
ENV HOME /work  

