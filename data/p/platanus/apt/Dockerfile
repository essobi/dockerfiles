FROM ubuntu:14.04  
  
MAINTAINER Juan Ignacio Donoso "juan.ignacio@platan.us"  
# Always use bash  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
# Update and install base packages  
RUN apt-get update && apt-get install -y \  
autoconf \  
build-essential \  
curl \  
git-core \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libmysqlclient-dev \  
libncurses-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  

