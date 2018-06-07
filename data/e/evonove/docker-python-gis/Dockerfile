FROM python:3.6  
# Base image for python applications using libgeos and libproj  
MAINTAINER Evoniners <dev@evonove.it>  
  
# Needed for pip  
ENV LC_ALL=C.UTF-8 LANG=C.UTF-8  
# Packages  
RUN apt-get update -qq && DEBIAN_FRONTEND=noninteractive apt-get install -y \  
binutils \  
gdal-bin \  
libproj-dev \  
libgeos-dev \  
netcat \  
> /dev/null && rm -rf /var/lib/apt/lists/*  
  
RUN pip3 install --quiet --upgrade setuptools  
  
# Install librdkafka  
ENV RDKAFKA_VERSION=0.11.0  
RUN curl -o /root/librdkafka-${RDKAFKA_VERSION}.tar.gz -SL
https://github.com/edenhill/librdkafka/archive/v${RDKAFKA_VERSION}.tar.gz && \  
tar -xzf /root/librdkafka-${RDKAFKA_VERSION}.tar.gz -C /root && \  
cd /root/librdkafka-${RDKAFKA_VERSION} && ./configure --prefix=/usr && make &&
make install  
  
# Directory where the code will be  
RUN mkdir -p /code  

