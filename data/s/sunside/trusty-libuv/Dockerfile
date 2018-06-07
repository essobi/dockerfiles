FROM ubuntu:trusty  
MAINTAINER Markus Mayer <awesome@everybag.de>  
  
RUN LIBUV_VERSION=1.11.0 \  
&& apt-get update \  
&& apt-get -y install vim-tiny nano curl wget autoconf automake build-
essential libtool \  
&& curl -sSL https://github.com/libuv/libuv/archive/v${LIBUV_VERSION}.tar.gz |
tar zxfv - -C /usr/local/src \  
&& cd /usr/local/src/libuv-$LIBUV_VERSION \  
&& sh autogen.sh && ./configure && make && make install \  
&& rm -rf /usr/local/src/libuv-$LIBUV_VERSION \  
&& ldconfig \  
&& apt-get -y purge autoconf automake build-essential libtool \  
&& apt-get -y autoremove \  
&& apt-get -y clean \  
&& rm -rf /var/lib/apt/lists/*  

