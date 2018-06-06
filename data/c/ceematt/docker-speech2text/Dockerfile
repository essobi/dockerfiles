# DOCKER-VERSION 1.4.0  
FROM ubuntu:14.04  
MAINTAINER Matt Snider (matt@cleanenergyexperts.com)  
  
RUN apt-get update  
  
# Sphinxbase  
RUN apt-get install -y gcc automake autoconf libtool bison swig python-dev
libpulse-dev git build-essential curl  
RUN mkdir sphinx-source && cd sphinx-source && git clone
https://github.com/cmusphinx/sphinxbase.git  
RUN cd sphinx-source/sphinxbase && ./autogen.sh && make && make install  
  
ENV LD_LIBRARY_PATH=/usr/local/lib  
  
# Pocket Sphinx  
RUN cd sphinx-source && git clone
https://github.com/cmusphinx/pocketsphinx.git  
RUN cd sphinx-source/pocketsphinx && ./autogen.sh && make && make install  
  
# python  
RUN apt-get install -y python python-pip  
  
# aws cli  
RUN pip install awscli

