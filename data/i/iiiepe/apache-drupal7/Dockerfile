FROM ubuntu:14.04  
MAINTAINER Luis Elizondo "lelizondo@gmail.com"  
ENV DEBIAN_FRONTEND noninteractive  
  
# Ensure UTF-8  
RUN locale-gen en_US.UTF-8  
ENV LANG en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
# Deny restarting applications when installing them  
RUN echo '#!/bin/sh\nexit 101' > /usr/sbin/policy-rc.d && chmod +x
/usr/sbin/policy-rc.d && \  
apt-get update && apt-get dist-upgrade -y && \  
apt-get -y install apache2 libapache2-mod-php5 php5-mcrypt php5-cli
php5-common php5-json \  
php5-memcache php5-mysql php5-gd php-pear php-apc php5-dev php5-curl curl git
supervisor make && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
pecl install uploadprogress && \  
/usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php && \  
/bin/mv composer.phar /usr/local/bin/composer && \  
apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* && \  
/usr/local/bin/composer self-update && \  
/usr/local/bin/composer global require drush/drush:6.* && \  
ln -s /.composer/vendor/drush/drush/drush /usr/local/bin/drush && \  
a2enmod php5 && \  
a2enmod rewrite && \  
sed -i 's/memory_limit = .*/memory_limit = 196M/' /etc/php5/apache2/php.ini &&
\  
sed -i 's/cgi.fix_pathinfo = .*/cgi.fix_pathinfo = 0/'
/etc/php5/apache2/php.ini && \  
sed -i 's/upload_max_filesize = .*/upload_max_filesize = 500M/'
/etc/php5/apache2/php.ini && \  
sed -i 's/post_max_size = .*/post_max_size = 500M/' /etc/php5/apache2/php.ini
&& \  
mkdir -p /etc/php5/conf.d && \  
echo "extension=uploadprogress.so" > /etc/php5/conf.d/uploadprogress.ini && \  
usermod -u 1000 www-data && \  
usermod -a -G users www-data && \  
chown -R www-data:www-data /var/www  
  
# Manually set up the apache environment variables  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/supervisor  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
  
EXPOSE 80  
WORKDIR /var/www  
VOLUME ["/var/www/sites/default/files"]  
CMD ["/usr/bin/supervisord", "-n"]  
  
# Add files  
ADD ./config/supervisord-apache.conf /etc/supervisor/conf.d/supervisord-
apache.conf  
ADD ./config/apache-config.conf /etc/apache2/sites-available/000-default.conf  

