FROM php:7.0-apache  
  
ENV DEBIAN_FRONTEND noninteractive  
  
COPY composer.json /var/www/html  
WORKDIR /var/www/html  
run TMP_PACKAGES="git zip" set -x \  
&& apt-get update \  
&& apt-get install -y ${TMP_PACKAGES} \  
&& cd /tmp \  
&& curl -ss https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& cd \- \  
&& composer require php-http/curl-client guzzlehttp/psr7 \  
&& composer install \  
&& apt-get --purge remove -y ${TMP_PACKAGES} \  
&& apt-get clean \  
&& (rm -f /var/cache/apt/archives/*.deb /var/cache/apt/archives/partial/*.deb
/var/cache/apt/*.bin || true)  
  
COPY mail.php /var/www/html/index.php  

