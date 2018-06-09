FROM php:7.0-cli  
MAINTAINER Sylvain Deloux <docker@eax.fr>  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_PROCESS_TIMEOUT 300  
RUN apt-get update && \  
apt-get install -y git wget zip unzip libicu-dev libmcrypt-dev libcurl3-dev
zlib1g-dev libssl-dev && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -s https://getcomposer.org/installer | php && \  
chmod +x composer.phar && \  
mv composer.phar composer && \  
mv composer /usr/bin  
  
RUN docker-php-ext-install intl  
RUN docker-php-ext-install ftp  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install opcache  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install zip  

