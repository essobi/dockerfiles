#change the sources.list  
FROM ubuntu:14.04  
MAINTAINER likang  
  
COPY sources.list /etc/apt/  
  
RUN apt-get update  
RUN apt-get install -y python python-pip python-dev libxml2-dev libxslt-dev
libffi-dev libssl-dev  
RUN pip install lxml && pip install pyopenssl && pip install Scrapy  

