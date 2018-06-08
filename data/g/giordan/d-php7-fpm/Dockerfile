# Debian: essential  
#  
# VERSION 0.1  
# Pull the base image.  
FROM giordan/d-essentials  
  
MAINTAINER Gabriele Giuranno <gabrielegiuranno@gmail.com>  
  
# Set environment variables.  
ENV FILES conf/  
ENV TERM xterm-256color  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >
/etc/apt/sources.list.d/dotdeb.list \  
&& curl -sS https://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get update \  
&& apt-get --no-install-recommends install -y \  
mysql-client \  
php7.0-cli \  
php7.0-fpm \  
php7.0-apcu \  
php7.0-apcu-bc \  
php7.0-curl \  
php7.0-json \  
php7.0-mcrypt \  
php7.0-opcache \  
php7.0-readline \  
php7.0-intl \  
php7.0-gd \  
php7.0-mysql \  
php7.0-xml  
  
RUN apt-get clean  
RUN rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ADD ${FILES}php-app.ini /etc/php/7.0/fpm/conf.d/  
ADD ${FILES}php-app.ini /etc/php/7.0/cli/conf.d/  
ADD ${FILES}php-app.pool.conf /etc/php/7.0/fpm/pool.d/  
  
RUN rm -rf /etc/php/7.0/fpm/pool.d/www.conf  
RUN usermod -u 1000 www-data  
  
ADD start.sh /usr/local/bin/start.sh  
  
# Configure executable to start php5-fpm.  
CMD ["start.sh"]  
  
# Expose ports.  
EXPOSE 9000  

