FROM python:3.5  
MAINTAINER Piter Oliveira Vergara <piter.vergara@code4fun.com.br>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PYTHONUNBUFFERED 1  
# Update and install packages recomended by Django documentation:  
# https://docs.djangoproject.com/ja/1.9/ref/contrib/gis/install/geolibs/  
# and extra needed packages  
RUN apt-get update -y && \  
apt-get install --auto-remove -y \  
binutils \  
libproj-dev \  
gdal-bin \  
postgis \  
curl \  
locales \  
apt-transport-https && \  
rm -rf /var/lib/apt/lists/*  
  
RUN echo 'en_US.UTF-8 UTF-8' >> /etc/locale.gen && /usr/sbin/locale-gen  
  
# Install nodejs 6.x  
RUN curl --silent https://deb.nodesource.com/gpgkey/nodesource.gpg.key | apt-
key add - && \  
echo "deb https://deb.nodesource.com/node_6.x jessie main" >
/etc/apt/sources.list.d/nodesource.list && \  
echo "deb-src https://deb.nodesource.com/node_6.x jessie main" >>
/etc/apt/sources.list.d/nodesource.list && \  
apt-get update && \  
apt-get install -y nodejs  
  
WORKDIR /usr/src/app  
  
ONBUILD COPY ./requirements.txt /requirements.txt  
ONBUILD RUN pip install -r /requirements.txt  
ONBUILD COPY . /usr/src/app  

