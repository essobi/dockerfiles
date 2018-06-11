FROM ubuntu:14.04  
MAINTAINER pipetc@gmail.com  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y \  
nginx \  
supervisor \  
curl \  
mercurial \  
git \  
gcc \  
g++ \  
nodejs \  
nodejs-legacy \  
npm \  
python-virtualenv \  
libgdal-dev \  
libpq-dev \  
python3-dev \  
libffi-dev \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  

