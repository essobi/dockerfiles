#  
# Apache Dockerfile - PHP 5.6  
#  
# https://github.com/rzani/Dockerfiles  
#  
FROM ubuntu:14.10  
MAINTAINER Rodrigo Zani <rodrigo.zhs@gmail.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get -yq install \  
curl \  
apache2 \  
libapache2-mod-php5 \  
memcached \  
php5 \  
php5-xdebug \  
php5-dev \  
php5-mysql \  
php5-gd \  
php5-imagick \  
php5-curl \  
php5-mcrypt \  
php5-memcached \  
php5-sqlite \  
php5-odbc \  
php5-pgsql  
  
RUN a2enmod rewrite && /etc/init.d/apache2 restart  
  
RUN rm -rf /var/lib/apt/lists/* /var/cache/apt/*  
  
# ===|=== to display errors  
RUN sed -i "s/display_errors = Off/display_errors = On/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/html_errors = Off/html_errors = On/" /etc/php5/apache2/php.ini  
  
COPY ./entrypoint.sh /  
# ===|=== my docker version (1.14) have a bug ()  
RUN chmod 0777 /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

