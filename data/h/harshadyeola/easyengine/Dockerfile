FROM ubuntu:14.04  
MAINTAINER Harshad Yeola <harshad.yeola@rtcamp.com>  
  
RUN /bin/bash  
RUN apt-get update  
RUN apt-get -y install wget  
RUN wget -qO ee rt.cx/ee && sudo bash ee  
RUN ee stack install  
RUN ee site create 1.com --html  
  

