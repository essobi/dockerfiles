FROM php:7-cli  
  
MAINTAINER Yannick Pereira-Reis <yannick.pereira.reis@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
curl \  
git \  
subversion \  
unzip \  
sudo \  
&& rm -r /var/lib/apt/lists/*  
  
RUN docker-php-ext-install mcrypt zip bz2 mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
RUN php --version  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# PRESTISSIMOOOOOOOOOO !!  
RUN composer global require hirak/prestissimo  
  
VOLUME ["/srv"]  
WORKDIR /srv  
  
##########################################################################################################  
# No ENTRYPOINT in my docker images to let people execute scripts or commands
before using the image tools  
##########################################################################################################  
CMD []  

