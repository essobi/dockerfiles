FROM node:6.11  
MAINTAINER Satoshi Ebihara <kiri@succhiello.net>  
  
RUN apt-get update \  
&& apt-get install -y --no-install-recommends \  
python3 \  
python3-dev \  
python3-pip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

