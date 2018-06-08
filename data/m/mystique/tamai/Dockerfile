##################################################################################  
##  
## VERSION : 0.0.1  
## DATE : 07Jan2016  
##  
## USAGE : Dockerfile to build scrapy in alpine linux  
## Ref [1] : https://hub.docker.com/r/trcook/docker-scrapy/~/dockerfile/  
## Ref [2] : https://github.com/shirk3y/scrapy-docker-
alpine/blob/master/Dockerfile  
##################################################################################  
  
FROM alpine:latest  
MAINTAINER mystique  
#RUN echo
"http://nl.alpinelinux.org/alpine/edge/testing">>/etc/apk/repositories  
RUN apk update  
RUN apk add python python-dev py-pip libxml2-dev libxslt-dev libffi-dev gcc
musl-dev openssl-dev libgcc \  
rm -rf /var/cache/apk/*;  
  
RUN pip install --upgrade pip; \  
pip install -U setuptools; \  
pip install scrapy;  
  
#CMD ["sh"]  
ENTRYPOINT ["/usr/bin/scrapy"]  

