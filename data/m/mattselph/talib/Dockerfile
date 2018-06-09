# TA-Lib Container on Ubuntu 16.04 LTS  
#  
# VERSION 0.0.1  
  
FROM ubuntu:16.04  
LABEL Description="This image is used to provide TA-Lib as an on-demand
service" Vendor="Tradelogic, LLC" Version="1.0"  
# install wget, compiler resources, and python  
RUN apt-get update && apt-get install -y build-essential wget python2.7
python-pip  
  
# get the TA-Lib source and build it  
RUN cd /root && wget https://s3.amazonaws.com/299934158332-pub/ta-
lib-0.4.0-src.tar.gz && tar -xzf ta-lib-0.4.0-src.tar.gz && cd ta-lib &&
./configure && make && make install  
# install the python TA-Lib API  
RUN cd /root && pip install --upgrade pip && pip install numpy && pip install
ta-lib  
# add LD_LIBRARY_PATH to .profile so TA-LIB imports correctly  
RUN echo "export LD_LIBRARY_PATH=/usr/local/lib" >> /root/.bashrc  

