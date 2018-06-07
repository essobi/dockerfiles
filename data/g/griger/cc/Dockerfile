FROM frolvlad/alpine-python3  
  
MAINTAINER Gustavo Rivas Gervilla <gustavo.rg92@gmail.com>  
  
RUN apk update && \  
echo http://dl-4.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
&& \  
apk add \--no-cache mongodb && \  
pip install --upgrade pip && \  
pip install Flask && \  
pip install Flask-PyMongo  

