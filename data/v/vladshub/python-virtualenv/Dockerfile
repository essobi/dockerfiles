FROM alpine  
MAINTAINER Vladislav Shub <vlad6il@gmail.com>  
  
ENV PYTHONIOENCODING utf-8  
RUN apk add --no-cache --update \  
python \  
python-dev \  
py-pip \  
build-base \  
git \  
openssl-dev \  
libxml2-dev \  
libxslt \  
libxslt-dev \  
py-libxslt \  
py-libxml2 \  
py-lxml \  
libssl1.0 \  
ca-certificates \  
wget \  
&& pip install --upgrade pip \  
&& pip install virtualenv \  
&& update-ca-certificates \  
&& rm -rf /var/cache/apk/*  
  
  

