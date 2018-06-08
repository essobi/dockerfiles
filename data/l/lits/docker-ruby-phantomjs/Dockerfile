FROM ruby:2.4.0  
### Replace shell with bash so we can source files ###  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
### install default sys packeges ###  
  
RUN apt-get update  
RUN apt-get install -qq -y \  
wget \  
sudo \  
git \  
curl \  
build-essential \  
rsync \  
imagemagick \  
libpq-dev \  
autoconf \  
libreadline-dev \  
libssl-dev \  
libxml2-dev \  
libxslt-dev \  
zlib1g-dev \  
libbz2-dev  
  
### install lts stable nodejs ###  
  
RUN apt-get install -y npm  
  
RUN npm cache clean -f && npm install -g n && n stable  
  

