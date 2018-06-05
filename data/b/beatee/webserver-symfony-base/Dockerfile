FROM ubuntu:xenial  
  
MAINTAINER Jan Klan <jan@beatee.org>  
  
RUN echo "\nexport TERM=xterm" >> ~/.bashrc  
  
RUN export TERM=xterm  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update \  
&& apt-get upgrade -y \  
&& apt-get install -y curl gettext supervisor git-core  
  
###  
# Install nginx  
###  
RUN apt-get install -y nginx  
  
###  
# Install PHP  
###  
RUN apt-get install -y \  
php7.0-fpm \  
php7.0-mcrypt \  
php7.0-curl \  
php7.0-mbstring \  
php7.0-mysql \  
php7.0-pspell \  
php7.0-sqlite \  
php7.0-xml \  
php7.0-gd \  
php7.0-intl \  
php-monolog \  
php-twig \  
php-imagick \  
php-memcached  
  
RUN phpenmod mcrypt  
  
###  
# Remove defaults  
###  
RUN rm /etc/php/7.0/fpm/pool.d/www.conf \  
&& rm /etc/nginx/sites-enabled/default \  
&& rm /etc/nginx/sites-available/default  
  
###  
# Add configuration files  
###  
ADD etc /etc  
  
RUN mkdir /run/php \  
&& ln -s /etc/nginx/sites-available/app.conf /etc/nginx/sites-enabled/app.conf  
  
EXPOSE 80  
###  
# Install composer  
###  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
###  
# Shrink image  
###  
RUN apt-get clean  
  
###  
# Set up entrypoint  
###  
CMD ["/usr/bin/supervisord", "-c", "/etc/supervisor/supervisord.conf"]  

