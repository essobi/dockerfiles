FROM python:3.6-alpine  
MAINTAINER Jesue Junior <jesuesousa@gmail.com>  
  
RUN apk add \--no-cache --virtual=build-dependencies --update build-base
python3-dev g++ make gcc linux-headers musl musl-dev libxml2 \  
libxml2-dev libxslt libxslt-dev py-mysqldb libpq postgresql-dev ca-
certificates && \  
apk del build-dependencies  
  

