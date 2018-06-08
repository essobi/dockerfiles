# Amazon Glacier CLI installed on Ubuntu  
FROM ubuntu:latest  
MAINTAINER Thomas Goldbrunner <thomas.goldbrunner@posteo.de>  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/folixg/docker.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0"  
  
# install git and pip  
RUN apt-get update && apt-get install -y python-pip git \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN git clone https://github.com/uskudnik/amazon-glacier-cmd-interface.git  
  
WORKDIR amazon-glacier-cmd-interface  
  
RUN python setup.py install  

