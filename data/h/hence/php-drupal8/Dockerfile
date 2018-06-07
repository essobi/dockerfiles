FROM hence/php:latest  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ENV COMPOSER_HOME=/root/.composer \  
TERM=xterm  
  
RUN apk --update add \  
git \  
mariadb-common \  
mariadb-client && \  
rm -rf /var/cache/apk/* && \  
composer global require drush/drush:8.1.2 && \  
composer global require fillup/phpmyadmin-minimal:4.4.13.1 && \  
ln -sf $COMPOSER_HOME/vendor/bin/drush.php /usr/bin/drush && \  
curl https://drupalconsole.com/installer -L -o drupal.phar && \  
mv drupal.phar /usr/bin/drupal && \  
chmod +x /usr/bin/drupal && \  
drupal init  
  
EXPOSE 22  
  
VOLUME ["/vendor", "/config"]  

