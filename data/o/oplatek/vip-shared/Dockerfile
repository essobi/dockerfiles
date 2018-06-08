FROM ubuntu:16.04  
MAINTAINER Ondrej Platek  
  
ENV clean_after_apt_get_install="rm -rf /var/lib/apt/lists/*"  
RUN apt-get update && \  
apt-get install -y \  
wget build-essential \  
python3 python3-dev python3-pip && \  
$clean_after_apt_get_install && \  
pip3 install --no-cache-dir --install-option="--zmq=bundled" pyzmq && \  
pip3 install --no-cache-dir \  
protobuf nose gevent && \  
locale-gen en_US.UTF-8  
  
ENV LANG en_US.UTF-8  
ENV LANGUAGE en_US:en  
ENV LC_ALL en_US.UTF-8  

