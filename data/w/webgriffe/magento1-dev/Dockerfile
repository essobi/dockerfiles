FROM webgriffe/php-apache-base:5.6  
MAINTAINER Webgriffe Srl <support@webgriffe.com>  
  
# Install n98-magerun  
RUN apt-get update \  
&& apt-get install -y wget  
  
RUN wget http://files.magerun.net/n98-magerun-latest.phar -O n98-magerun.phar
\  
&& chmod +x ./n98-magerun.phar \  
&& mv ./n98-magerun.phar /usr/local/bin/  
  
# Install mysql-client (required by n98-magerun db commands)  
RUN apt-get update \  
&& apt-get install -y mysql-client  
  
# Install Memcached PHP extension (useful for Magento cache & session storage)  
RUN apt-get install -y libmemcached-dev \  
&& pecl install memcached-2.2.0 \  
&& docker-php-ext-enable memcached  

