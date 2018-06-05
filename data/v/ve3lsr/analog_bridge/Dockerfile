FROM phusion/baseimage  
MAINTAINER projects@ve3lsr.ca  
  
RUN apt-get update && apt-get install -yq git libsndfile1 libasound2 && apt-
get clean && rm -rf /var/lib/apt/lists/* /var/tmp/* /tmp/*  
  
WORKDIR /opt/  
  
RUN git clone https://github.com/N4IRS/Analog_Bridge.git  
  
WORKDIR /opt/Analog_Bridge  
  
# CMD ./hblink.py  

