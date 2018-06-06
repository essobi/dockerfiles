FROM ruby:2.3.0-slim  
MAINTAINER Eric Hartmann <hartmann.eric@gmail.com>  
  
RUN apt-get update && apt-get upgrade -y  
RUN apt-get install -qqy \  
build-essential \  
wget \  
curl \  
make \  
gcc \  
locales  
  
RUN dpkg-reconfigure locales && \  
locale-gen C.UTF-8 && \  
/usr/sbin/update-locale LANG=C.UTF-8  
ENV LC_ALL C.UTF-8  
  
COPY . /cryptcheck  
  
# Custom OpenSSL build, time to grab a coffee  
RUN cd /cryptcheck ; \  
make ; \  
bundle install  
  
  
WORKDIR /cryptcheck/bin  

