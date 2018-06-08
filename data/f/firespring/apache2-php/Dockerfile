FROM ubuntu:14.04  
MAINTAINER Jeffery Utter "jeff.utter@firespring.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN mkdir -p /var/run/apache2 /var/lock/apache2  
  
RUN apt-get update \  
&& apt-get install -y \  
# Apache\PHP  
apache2 libapache2-mod-gnutls php5 php5-mysql php5-curl php5-xcache php-pear
php5-gd php-xml-parser php5-dev \  
# Mogile  
libpcre3-dev libxml2-dev libneon27-dev \  
# Build Deps  
build-essential curl make \  
# Other Deps  
pdftk zip \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN curl -s -o phpunit-3.7.31.phar https://phar.phpunit.de/phpunit-3.7.31.phar
\  
&& chmod 777 phpunit-3.7.31.phar \  
&& mv phpunit-3.7.31.phar /usr/local/bin/phpunit  
  
RUN pecl install xdebug-2.2.6 \  
&& pear install PHP_CodeSniffer \  
&& pecl install memcache \  
&& pecl install redis-2.2.8 \  
&& pecl install zip \  
&& pecl install mogilefs-0.9.2  
  
RUN a2enmod ssl \  
&& a2enmod php5 \  
&& a2enmod rewrite \  
&& a2enmod headers  
  
RUN a2dissite 000-default  
RUN a2dismod autoindex  
  
RUN curl -sS https://getcomposer.org/installer | php && mv composer.phar
/usr/local/bin/composer  
  
# Apache Config  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APPLICATION_ENV local  
  
COPY apache2/apache2.conf /etc/apache2/  
COPY php/conf.d/ /etc/php5/apache2/conf.d/  
COPY php/conf.d/ /etc/php5/cli/conf.d/  
  
COPY apache2-foreground /usr/local/bin/  
  
ENV SERVER_NAME=localhost  
ENV APACHE_RUN_USER=www-data  
ENV APACHE_RUN_GROUP=www-data  
ENV APACHE_PID_FILE=/var/run/apache2/apache2.pid  
ENV APACHE_RUN_DIR=/var/run/apache2  
ENV APACHE_LOCK_DIR=/var/lock/apache2  
ENV APACHE_LOG_DIR=/var/log/apache2  
ENV APACHE_LOG_LEVEL=warn  
ENV APACHE_CUSTOM_LOG_FILE=/proc/self/fd/1  
ENV APACHE_ERROR_LOG_FILE=/proc/self/fd/2  
CMD ["apache2-foreground"]  

