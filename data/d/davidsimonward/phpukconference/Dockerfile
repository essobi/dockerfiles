FROM php:7.1.0-fpm  
  
#
-----------------------------------------------------------------------------  
# SET CORRECT TIMEZONE  
#
-----------------------------------------------------------------------------  
RUN mv /etc/localtime /etc/localtime.bak \  
&& ln -s /usr/share/zoneinfo/Europe/London /etc/localtime  
  
#
-----------------------------------------------------------------------------  
# SERVICES & PHP EXTENSIONS  
#
-----------------------------------------------------------------------------  
RUN \  
apt-get update && \  
apt-get install -y \  
git  
  
#
-----------------------------------------------------------------------------  
# COMPOSER INSTALLATION  
#
-----------------------------------------------------------------------------  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
#
-----------------------------------------------------------------------------  
# COPY composer files  
#
-----------------------------------------------------------------------------  
COPY /appcode/composer.json /var/www/html  
COPY /appcode/composer.lock /var/www/html  
  
#
-----------------------------------------------------------------------------  
# Composer install before the cache is invalidated by the new application
source files;  
# Our dependencies will not be downloaded with every Docker build.  
# However, without the source files we cannot run our composer scripts  
# or build the autoloader just yet, so we use the --no-scripts and --no-
autoloader flags.  
#
-----------------------------------------------------------------------------  
RUN composer install --no-scripts --no-autoloader  
  
#
-----------------------------------------------------------------------------  
# Add Application Code  
#
-----------------------------------------------------------------------------  
COPY /appcode /var/www/html  
  
#
-----------------------------------------------------------------------------  
# Only after we have copied all the source files, we dump the autoloader and
run the scripts.  
#
-----------------------------------------------------------------------------  
RUN composer dump-autoload --optimize  

