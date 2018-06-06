FROM dans00/docker-confd:latest  
MAINTAINER Dan Sloan <dan@dansloan.org>  
  
# Update package index when we install mariadb  
RUN apk add --update php-fpm php-mysqli php php-gd php-apcu php-cli php-pear
php-gmp php-pcntl php-curl php-iconv php-ldap php-json php-xml php-phpmailer
git  
  
COPY docker-init /docker-init  
  
# Ports exposed for this container  
EXPOSE 8080 8443  

