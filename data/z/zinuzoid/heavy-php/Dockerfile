FROM php:5.6-apache  
MAINTAINER Jetsada Machom <jim@imjim.im>  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
vim \  
libmcrypt-dev \  
libssl-dev \  
mongodb-clients \  
mysql-client \  
php5-cgi \  
php5-mysql \  
php5-mcrypt \  
php5-mongo \  
php-amqplib && \  
docker-php-ext-install \  
bcmath \  
pdo \  
pdo_mysql \  
mysql \  
mcrypt \  
zip && \  
pecl install bcmatch mongo mongodb && \  
echo "extension=mongo.so" > /usr/local/etc/php/conf.d/ext-mongo.ini && \  
echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongodb.ini && \  
curl -s -o /usr/local/bin/composer https://getcomposer.org/composer.phar && \  
chmod 0755 /usr/local/bin/composer  
  

