FROM ubuntu:latest  
  
MAINTAINER Ludovic Meurillon <ludovic.meurillon@orange.com>  
  
RUN apt-get -y update \  
&& apt-get install -y python python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install robotframework-hub==0.8.3  
  
RUN mkdir /robot  
VOLUME /robot  
WORKDIR /robot  
  
EXPOSE 7070  
ENTRYPOINT ["/usr/bin/python", "-m", "rfhub", "-i", "0.0.0.0", "/robot"]

