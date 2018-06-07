#  
# NOTE: FILE GENERATED VIA "update.sh"  
#  
# PLEASE DO NOT EDIT IT DIRECTLY  
#  
FROM php:7.1-cli-jessie  
MAINTAINER Paweł Tomulik <ptomulik@meil.pw.edu.pl>  
  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
libldap2-dev \  
libsasl2-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
curl -L
https://github.com/jwilder/dockerize/releases/download/v0.6.0/dockerize-linux-
amd64-v0.6.0.tar.gz \  
\--output /tmp/dockerize-linux-amd64-v0.6.0.tar.gz && \  
tar -C /usr/local/bin -zxvf /tmp/dockerize-linux-amd64-v0.6.0.tar.gz && \  
rm -f /tmp/dockerize-linux-amd64-v0.6.0.tar.gz && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu \--with-ldap-
sasl && \  
docker-php-ext-install ldap  
  
# vim: set ft=dockerfile:  

