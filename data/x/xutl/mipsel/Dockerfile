FROM ubuntu:xenial  
  
LABEL maintainer="xutongle@gmail.com"  
  
WORKDIR /app  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
g++-mipsel-linux-gnu gcc-mipsel-linux-gnu \  
gettext build-essential autoconf libtool libpcre3-dev asciidoc xmlto \  
libev-dev libc-ares-dev automake libmbedtls-dev libsodium-dev \  
wget git ca-certificates openssl \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

