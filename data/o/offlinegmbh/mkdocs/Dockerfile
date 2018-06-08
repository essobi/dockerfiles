FROM python:2.7-alpine  
  
MAINTAINER Tobias Kuendig <tobias@offline.swiss>  
  
RUN apk update; \  
apk add python2-dev ; \  
pip install mkdocs pygments pymdown-extensions mkdocs-material  
  
RUN mkdir /docs  
  
WORKDIR /docs  

