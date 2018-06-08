FROM ubuntu:trusty  
MAINTAINER Alexandre Dias <alex.jm.dias@gmail.com>  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update  
  
RUN apt-get -y install git curl wget \  
mariadb-client mariadb-server apache2 libapache2-mod-php5 \  
python-setuptools memcached php5-memcache \  
php5-cli php5-mysql php-apc php5-gd php5-curl php5-xdebug; \  
apt-get clean; \  
apt-get autoclean; \  
apt-get -y autoremove  
  
# Install Composer & Drush  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Install Drush, Drupal Console and pimp-my-log  
RUN HOME=/ /usr/local/bin/composer global require drush/drush:dev-master; \  
HOME=/ /usr/local/bin/composer global require drupal/console:dev-master; \  
HOME=/ /usr/local/bin/composer require "potsky/pimp-my-log"  
RUN HOME=/ /usr/local/bin/composer global require drush/drush:dev-master  
  
#Xdebug  
ADD ./files/xdebug.ini /etc/php5/mods-available/xdebug.ini  
  
# Display version information  
RUN php --version  
RUN composer --version  
RUN /.composer/vendor/drush/drush/drush --version && ln -s
/.composer/vendor/drush/drush/drush /usr/bin/drush  
  
# Drupal new version, clean cache  
ADD https://www.drupal.org/project/drupal /tmp/latest.html  
  
#Manage db with adminer  
RUN wget "http://www.adminer.org/latest.php" -O /var/www/html/adminer.php

