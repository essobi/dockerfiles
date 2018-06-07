FROM php:7-cli  
  
MAINTAINER Scott Wilcox <scott@dor.ky>  
  
# exit if a command fails  
RUN set -e  
  
# Stop upstart from complaining  
RUN dpkg-divert --local \--rename --add /sbin/initctl  
RUN ln -sf /bin/true /sbin/initctl  
ENV DEBIAN_FRONTEND noninteractive  
  
# Dependancies for extensions  
RUN apt-get update -yqq  
RUN apt-get install git zip libicu-dev libpng-dev libjpeg-dev libbz2-dev
libfontconfig xvfb libxrender1 libxrender-dev -yqq  
  
# Install extensions  
RUN docker-php-ext-install intl gd bz2 pdo_mysql pcntl  
  
# Installer composer  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer && chmod +x /usr/local/bin/composer  
  
# Cleanup  
RUN apt-get remove --purge -y curl build-essential && apt-get autoclean &&
apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

