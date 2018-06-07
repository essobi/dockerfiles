FROM debian:jessie  
MAINTAINER Chris Kanich <kaytwo@gmail.com>  
  
ENV BUILD_PACKAGES "python-pip python-dev libxml2-dev libxslt1-dev zlib1g-dev
libffi-dev libssl-dev"  
ENV RUN_PACKAGES "libxslt1.1 python python-six python-openssl python-
configparser python-service-identity"  
RUN apt-get update && apt-get install -y $BUILD_PACKAGES && pip install Scrapy
&& apt-get remove --purge -y $BUILD_PACKAGES $(apt-mark showauto) && apt-get
install -y $RUN_PACKAGES && rm -rf /var/lib/apt/lists/*  
  
# create working directory  
RUN mkdir /app  
  
# change working directory  
WORKDIR /app  

