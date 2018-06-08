# Copyleft (ↄ) 2016 Thiago Almeida <thiagoalmeidasa@gmail.com>  
#  
# Distributed under terms of the GPLv2 license.  
FROM php:7-fpm  
  
MAINTAINER Thiago Almeida <thiagoalmeidasa@gmail.com>  
  
  
ENV SSP_VERSION 1.0  
ENV SSP_URL https://github.com/ltb-project/self-service-
password/archive/v${SSP_VERSION}.tar.gz  
  
#####  
# SYSTEM REQUIREMENT  
#####  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libldap2-dev libmcrypt-dev && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap mbstring mcrypt  
  
RUN cd /var/www/ && \  
curl -SL $SSP_URL | tar -xz -C /var/www/ && \  
mv self-service-password-${SSP_VERSION}/* html/ && \  
rm -rf self-service-password-${SSP_VERSION}  
  
COPY config.inc.php.template /config.inc.php.template  
COPY entrypoint.sh /entrypoint.sh  
RUN chmod +x /entrypoint.sh  
  
VOLUME /var/www/html  
  
ENTRYPOINT /entrypoint.sh  

