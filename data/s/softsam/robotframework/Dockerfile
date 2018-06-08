FROM ubuntu:latest  
  
MAINTAINER Ludovic Meurillon <ludovic.meurillon@orange.com>  
  
RUN apt-get -y update \  
&& apt-get install -y python python-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN pip install robotframework==2.9  
RUN pip install robotframework-selenium2library==1.7.2  
RUN pip install robotframework-appiumlibrary==1.3.5  
RUN pip install robotframework-faker==3.0.0  
  
RUN mkdir /robot  
VOLUME /robot  
WORKDIR /robot  

