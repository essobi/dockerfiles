FROM owncloud:9.0  
MAINTAINER Hauke Mettendorf <hauke.mettendorf@iteratec.de>  
  
# Install ldap requirements  
RUN \  
apt-get update && \  
apt-get install libldap2-dev -y && \  
rm -rf /var/lib/apt/lists/* && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  
VOLUME ["/var/www/html/config", "/var/www/html/data"]  
  
EXPOSE 80 443  

