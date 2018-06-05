FROM ubuntu:16.04  
MAINTAINER Wela Dev Team <developer@getwela.com>  
  
  
### Install basic software utilities  
####################################  
  
RUN apt-get update && apt-get install -y \  
software-properties-common  
  
RUN apt-get update && apt-get install -y \  
python-software-properties  
  
  
### Add a php7.1 repo & Install necessary dependencies  
######################################################  
  
# Install locales  
RUN apt-get update && apt-get install -y \  
locales  
RUN locale-gen en_US.UTF-8 && export LANG=en_US.UTF-8  
RUN LC_ALL=C.UTF-8 add-apt-repository -y ppa:ondrej/php  
  
RUN apt-get update && apt-get install -y sudo && rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
software-properties-common \  
python-software-properties \  
openssh-client \  
curl \  
ca-certificates \  
wget \  
apache2 \  
curl \  
git \  
nginx \  
php7.1 \  
php7.1-cli \  
php7.1-mbstring \  
php7.1-mongodb \  
php7.1-mysql \  
php7.1-xml \  
php7.1-zip \  
php7.1-gd \  
php7.1-mcrypt \  
php7.1-dom \  
php7.1-xdebug \  
php7.1-fpm \  
php-curl \  
  

