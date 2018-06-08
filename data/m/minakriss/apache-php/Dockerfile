FROM debian:stable  
MAINTAINER Jeb Steel <minakriss.rogue@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive \  
&& apt-get update \  
&& apt-get -y install \  
apache2 \  
php-apc \  
php-date \  
php-db \  
php-gettext \  
php-services-json \  
php-soap \  
php-xajax \  
php5 \  
php5-cli \  
php5-common \  
php5-curl \  
php5-gd \  
php5-imagick \  
php5-intl \  
php5-ldap \  
php5-mcrypt \  
php5-memcache \  
php5-memcached \  
php5-mysql \  
php5-pgsql \  
php5-sqlite \  
php5-xdebug \  
php5-xmlrpc \  
&& \  
apt-get clean \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
RUN /usr/sbin/a2dismod 'mpm_*' && /usr/sbin/a2enmod mpm_prefork  
  
RUN a2enmod php5  
RUN a2enmod rewrite  
  
ENV APACHE_RUN_USER=www-data  
ENV APACHE_RUN_GROUP=www-data  
ENV APACHE_LOG_DIR=/var/log/apache2  
ENV APACHE_LOCK_DIR=/var/lock/apache2  
ENV APACHE_PID_FILE=/var/run/apache2.pid  
  
COPY config/000-default.conf /etc/apache2/sites-available/000-default.conf  
  
EXPOSE 80  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

