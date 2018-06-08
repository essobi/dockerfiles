# Composer Docker Container  
# Base Dockerfile: composer/base  
FROM php:5.6-cli  
MAINTAINER Grafikart <contact@grafikart.fr>  
  
# Packages  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
wget \  
curl \  
git \  
&& rm -r /var/lib/apt/lists/*  
  
# PHP Extensions  
RUN docker-php-ext-install mcrypt zip bz2 mbstring  
  
# Memory Limit  
RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini  
  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
/usr/local/etc/php/conf.d/date_timezone.ini  
  
# Environmental Variables  
RUN wget http://rocketeer.autopergamene.eu/versions/rocketeer.phar  
RUN chmod +x rocketeer.phar  
RUN mv rocketeer.phar /usr/local/bin/rocketeer  
  
# Display rocketeer version  
# Set up the application directory  
VOLUME ["/app"]  
WORKDIR /app  
  
# Set up the command arguments  
ENTRYPOINT ["rocketeer"]

