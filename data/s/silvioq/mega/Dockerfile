FROM debian:jessie  
MAINTAINER silvioq@gmail.com  
  
RUN apt-get update -qq && apt-get install -y \  
autoconf \  
build-essential \  
git \  
libtool \  
libc-ares-dev \  
libcrypto++-dev \  
libcurl4-openssl-dev \  
libfuse-dev \  
libsqlite3-dev \  
libssl-dev \  
libreadline-dev \  
libfreeimage-dev \  
&& rm -rf /var/lib/apt/lists/* \  
&& git clone https://github.com/meganz/sdk.git \  
&& cd sdk \  
&& sh autogen.sh \  
&& ./configure --with-fuse \  
&& make \  
&& make install \  
&& cd / \  
&& rm -fr sdk \  
&& ldconfig  

