FROM debian:jessie-backports  
MAINTAINER Henri Menke <henrimenke.com>  
ENV DEBIAN_FRONTEND noninteractive  
RUN apt-get update \  
&& apt-get install --no-install-recommends -t jessie-backports -y \  
cmake build-essential git \  
libarmadillo-dev \  
libboost-test-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

