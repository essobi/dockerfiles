FROM hence/php:latest  
MAINTAINER Clint Beacock <clint@therefore.ca>  
  
ENV COMPOSER_HOME=/root/.composer \  
TERM=xterm  
  
RUN apk --update add \  
git \  
mariadb-common \  
mariadb-client && \  
rm -rf /var/cache/apk/* && \  
composer global require drush/drush:6.6.0 && \  
composer global require fillup/phpmyadmin-minimal:4.4.13.1 && \  
ln -sf $COMPOSER_HOME/vendor/bin/drush.php /usr/bin/drush  
  
EXPOSE 22  
  
VOLUME ["/vendor"]  

