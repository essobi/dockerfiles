FROM debian:stretch  
MAINTAINER Colin Bennett <colin@gibibit.com>  
ARG DEBIAN_FRONTEND=noninteractive  
COPY dpkg-nodoc.conf /etc/dpkg/dpkg.conf.d/01_nodoc  
COPY remove-docs.sh /tmp/remove-docs.sh  
RUN apt-get update && apt-get install -y \  
build-essential \  
cmake \  
ninja-build \  
&& sh /tmp/remove-docs.sh \  
&& rm -rf /tmp/* && rm -rf /var/lib/apt/lists/*  

