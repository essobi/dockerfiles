FROM jenkins:alpine  
MAINTAINER Valery M. <vamukhs@gmail.com>  
  
USER root  
  
RUN apk add \--no-cache python && \  
python -m ensurepip && \  
rm -r /usr/lib/python*/ensurepip && \  
pip install --upgrade pip setuptools requests && \  
rm -r /root/.cache  
  
USER jenkins  

