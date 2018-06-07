FROM ubuntu:16.04  
  
MAINTAINER Yuta Fukasawa <yuta.fukasawa28@gmail.com>  
  
RUN apt-get update \  
&& apt-get install python3-pip python3-dev -y \  
&& pip3 install --upgrade pip \  
&& pip3 install tensorflow==1.3.0rc0 \  
&& pip3 install tflearn  

