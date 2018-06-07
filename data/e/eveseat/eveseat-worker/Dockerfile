FROM php:7.1-alpine  
  
RUN apk add --no-cache \  
# Install OS level dependencies  
git zip unzip curl \  
libpng-dev libmcrypt-dev bzip2-dev icu-dev mariadb-client && \  
# Install PHP dependencies  
docker-php-ext-install pdo_mysql gd bz2 intl mcrypt pcntl  
  
COPY startup.sh /root/startup.sh  
RUN chmod +x /root/startup.sh  
  
VOLUME "/var/www/seat"  
WORKDIR /var/www/seat  
  
ENTRYPOINT ["/bin/sh", "/root/startup.sh"]  

