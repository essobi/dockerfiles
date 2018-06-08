FROM php:7.1-fpm-alpine  
MAINTAINER timothy.teoh@frogasia.com  
  
RUN sed -i -e 's/v3\\.4/v3.5/g' /etc/apk/repositories  
RUN apk --no-cache add \  
curl \  
libmcrypt-dev \  
libmcrypt \  
mysql-client \  
wget  
  
RUN docker-php-ext-install \  
mcrypt \  
mbstring \  
mysqli \  
pcntl \  
pdo_mysql  
  
EXPOSE 9000  
CMD ["php-fpm", "-F"]  
  

