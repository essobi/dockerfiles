FROM ubuntu:xenial  
MAINTAINER Vasileios Karavasilis <vasileioskaravasilis@gmail.com>  
  
RUN apt-get -qq update \  
&& apt-get -qqy install \  
python3 python3-pip \  
&& python3 -m pip install nose pymongo jsonpickle requests requests_mock
python-dateutil \  
&& rm -rf /var/lib/apt/lists/*  

