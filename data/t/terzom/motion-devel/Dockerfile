FROM ubuntu:16.04  
MAINTAINER Mike Terzo <mike@terzo.org>  
  
# Here's a comment for chris.  
  
RUN apt-get -y update && apt-get install -y \  
autoconf \  
build-essential \  
autoconf \  
automake \  
git \  
pkg-config \  
libtool \  
libjpeg8-dev \  
libzip-dev \  
libavformat-dev \  
libavcodec-dev \  
libswscale-dev \  
libv4l-dev \  
libmysqlclient-dev \  
libpq-dev \  
libsqlite3-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
CMD bash  

