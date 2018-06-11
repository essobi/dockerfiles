#
########################################################################################  
# PHP IMAGE WATCHER  
#  
# This is a stand-alone container utilizing PHP 7 designed to be able to
consolidate  
# images from multiple sources and place those images into a repository.  
#  
# Please see the sample.env contained within this repository for information
on the  
# necessary environment configuration required to run this software  
#  
#  
  
FROM php:7-cli  
  
MAINTAINER Christopher Scheidel <cscheide@oiltycoonsllc.com>  
  
# Update and install system dependencies  
RUN apt-get update && apt-get install -y \  
libmagickwand-dev \  
unzip \  
git \  
&& rm -rf /var/lib/apt/lists/*  
  
# Install imagick and enable it  
RUN pecl install imagick && docker-php-ext-enable imagick  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Install the code  
RUN mkdir /usr/src/app  
COPY src/* /usr/src/app/  
WORKDIR /usr/src/app  
  
# Get vendor files  
RUN cd /usr/src/app && composer update  
  
# Run the app when launched  
CMD [ "php", "./app.php" ]  

