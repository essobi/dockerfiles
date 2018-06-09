FROM ubuntu:latest  
  
MAINTAINER Thomas Nabord <thomas.nabord@prestashop.com>  
  
  
RUN apt-get update \  
&& apt-get install --no-install-recommends -y \  
nodejs \  
npm \  
php7.0-cli \  
php7.0-curl \  
php7.0-json \  
php7.0-intl \  
curl \  
wget \  
git \  
&& apt-get clean \  
&& rm -r /var/lib/apt/lists/*  
  
RUN ln -sf /usr/bin/nodejs /usr/bin/node && npm install -g grunt-cli  
  
ENTRYPOINT ["/tmp/docker_run.sh"]  

