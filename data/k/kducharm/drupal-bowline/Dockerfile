#  
# Drupal  
# - also includes Composer, MySQL Client, and Drush  
#  
FROM drupal  
MAINTAINER Kristian Ducharme <kristian.ducharme@civicactions.com>  
  
# Packages.  
RUN apt-get update && \  
apt-get -y install git mysql-client wget curl \  
pwgen sudo python-setuptools nano apt-utils tidy vim pv mysql-client && \  
apt-get autoclean && apt-get autoremove  
  
# whitelist = phar  
RUN \  
mkdir -p /etc/php5/conf.d/ && \  
echo "suhosin.executor.include.whitelist = phar" >>
/etc/php5/conf.d/suhosin.ini  
  
# Composer.  
RUN \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin -d detect_unicode=0 && \  
ln -s /usr/local/bin/composer.phar /usr/local/bin/composer  
  
# Sudo.  
RUN echo %sudo ALL=NOPASSWD: ALL >> /etc/sudoers  
  
# Scripts.  
ADD ./conf/scripts/start.sh /start.sh  
ADD ./conf/scripts/foreground.sh /etc/apache2/foreground.sh  
  
# Apache.  
RUN rm -rf /var/www/*  
RUN chmod 755 /etc/apache2/foreground.sh  
RUN chmod 755 /start.sh  
  
# Apache / PHP.  
ADD ./conf/apache2/vhost.conf /etc/apache2/sites-available/000-default.conf  
ADD ./conf/php7/bowline-php.ini /usr/local/etc/php/conf.d/bowline-php.ini  
  
# Xdebug settings.  
RUN pecl install xdebug-2.5.0 \  
&& docker-php-ext-enable xdebug  
RUN \  
echo xdebug.remote_enable=1 >> /usr/local/etc/php/conf.d/xdebug.ini && \  
echo xdebug.remote_autostart=0 >> /usr/local/etc/php/conf.d/xdebug.ini && \  
echo xdebug.idekey="PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini && \  
echo xdebug.max_nesting_level=256 >> /usr/local/etc/php/conf.d/xdebug.ini && \  
echo xdebug.remote_log=/var/www/logs/xdebug.log >>
/usr/local/etc/php/conf.d/xdebug.ini  
  
EXPOSE 80  
# Set a custom entrypoint.  
COPY ./docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  

