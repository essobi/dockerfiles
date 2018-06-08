FROM phusion/baseimage:0.10.1  
  
LABEL maintainer="nick@foobar.net.nz"  
RUN apt-get update -qqy \  
&& DEBIAN_FRONTEND=noninteractive apt-get install -qqy \  
php-fpm \  
php-curl \  
php-gd \  
php-http \  
php-imagick \  
php-json \  
php-log \  
php-mbstring \  
php-memcache \  
php-mysqli \  
php-oauth \  
&& apt-get clean -qqy  
  
# Configure a service entry for Apache  
COPY run /etc/service/php-fpm/run  
  
COPY logging.ini /etc/php/7.0/mods-available/logging.ini  
  
# Enable for FPM  
RUN phpenmod logging curl gd imagick json mbstring memcache mysqli oauth
opcache  
  
# Test the Configuration  
RUN /etc/service/php-fpm/run -t 2>&1  
  
EXPOSE 9000  

