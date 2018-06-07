FROM python:3.5  
MAINTAINER Parrot Prediction <contact@parrotprediction.com>  
  
ENV SCRAPY_VERSION "1.2.1"  
RUN pip3.5 install scrapy==$SCRAPY_VERSION  
  
RUN mkdir -p /data  
VOLUME /data  
WORKDIR /data  

