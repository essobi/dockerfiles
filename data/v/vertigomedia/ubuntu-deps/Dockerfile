FROM ubuntu:14.04  
MAINTAINER Dan Fowler <dan@logickc.com>  
  
#Let people know how this was built  
ADD Dockerfile /root/Dockerfile  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
git \  
openssh-client \  
autoconf \  
build-essential \  
software-properties-common \  
imagemagick \  
libbz2-dev \  
libcurl4-openssl-dev \  
libevent-dev \  
libffi-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblzma-dev \  
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
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  

