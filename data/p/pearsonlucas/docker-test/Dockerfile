FROM ubuntu:15.04  
MAINTAINER Lucas Pearson <pearson.lucas.dev@gmail.com>  
  
RUN apt-get update && apt-get -y install \  
apache2 \  
php5 \  
php5-cli \  
php5-curl \  
php5-mongo \  
php5-ldap \  
php5-mysql \  
git \  
python \  
python-setuptools \  
python-dev \  
build-essential \  
curl \  
ssh \  
mysql-client \  
vim  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer && composer self-update  

