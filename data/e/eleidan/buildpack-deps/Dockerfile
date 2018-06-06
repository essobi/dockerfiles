FROM eleidan/buildpack-deps-scm:ubuntu-16.04  
  
LABEL maintainer="Oleg Kulyk" \  
description="Ubuntu 16.04, buildpack-deps" \  
run="docker run -it --rm -v $(pwd):/home/phantom/app eleidan/buildpack-
deps:ubuntu-16.04" \  
version="2017-07-09"  
  
ENV SERVICE_NAME="buildpack-deps:ubuntu-16.04"  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
autoconf \  
automake \  
bash-completion \  
bzip2 \  
file \  
g++ \  
gcc \  
imagemagick \  
libbz2-dev \  
libc6-dev \  
libcurl4-openssl-dev \  
libdb-dev \  
libevent-dev \  
libffi-dev \  
libgeoip-dev \  
libglib2.0-dev \  
libjpeg-dev \  
liblzma-dev \  
libmagickcore-dev \  
libmagickwand-dev \  
libncurses-dev \  
libpng-dev \  
libpq-dev \  
libreadline-dev \  
libsqlite3-dev \  
libssl-dev \  
libtool \  
libwebp-dev \  
libxml2-dev \  
libxslt-dev \  
libyaml-dev \  
make \  
patch \  
xz-utils \  
zlib1g-dev \  
&& rm -rf /var/lib/apt/lists/*  

