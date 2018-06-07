FROM jeeva420/alpine-base  
MAINTAINER Jeeva Kailasam <kjeeva@ymail.com>  
  
# Set correct environment variables  
ARG BASE_APKLIST="python3"  
ARG PIP_LIST="mkdocs mkdocs-material mkdocs-windmill pymdown-extensions"  
# install main packages  
RUN apk add \--no-cache $BASE_APKLIST && \  
pip3 install $PIP_LIST  
# add local files  
COPY /root /  
  
# expose ports  
EXPOSE 8000  
# set volumes  
VOLUME /config  

