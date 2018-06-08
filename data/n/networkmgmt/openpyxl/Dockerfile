FROM python:3.6-alpine  
MAINTAINER Tsubasa Nagano <networkmgmt [at] icloud.com>  
  
RUN apk update  
  
RUN apk --no-cache add \  
build-base \  
jpeg-dev \  
zlib-dev  
  
RUN pip --no-cache-dir install \  
openpyxl \  
pillow  
  
WORKDIR /var/openpyxl/  

