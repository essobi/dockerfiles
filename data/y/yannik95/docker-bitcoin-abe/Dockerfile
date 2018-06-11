#!/bin/sh  
# testnet docker image  
# Use phusion/baseimage as base image. To make your builds reproducible, make  
# sure you lock down to a specific version, not to `latest`!  
# See https://github.com/phusion/baseimage-docker/blob/master/Changelog.md for  
# a list of version numbers.  
FROM phusion/baseimage  
MAINTAINER Yannik Eichel <docker@yannikeichel.de>  
ENV REFRESHED_AT 20171218  
# Use baseimage-docker's init system.  
CMD ["/sbin/my_init"]  
  
# install python  
RUN apt-get -yqq update  
RUN apt-get -yqq install git sqlite sudo wget python-dev python-flup python-
crypto  
  
# Clean up APT when done.  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
# git clone bitcoin-abe to be a local block explorer  
WORKDIR /home  
RUN git clone https://github.com/bitcoin-abe/bitcoin-abe  
  
# build bitcoin-abe, it requires a patch to be run within docker  
WORKDIR /home/bitcoin-abe  
ADD ./bitcoinabe.abe.py.patch /home/bitcoin-abe/abe.py.patch  
RUN patch -p1 < abe.py.patch  
RUN python setup.py install  
  
ADD ./db.conf /home/bitcoin-abe/  
ADD ./run.server.sh /home/bitcoin-abe/  
  
RUN chmod 755 /home/bitcoin-abe run.server.sh  
  
EXPOSE 80  
CMD ["/home/bitcoin-abe/run.server.sh"]  

