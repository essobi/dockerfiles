FROM otassel/php-apache:ubuntu-15.10  
MAINTAINER Olivier TASSEL <olivier.tassel@investissima.com>  
  
COPY apache/config/000-default.conf /etc/apache2/sites-available/  
#COPY apache/ssl/* /etc/apache2/certs/  
COPY silex /var/www  
  
# Request Apache module enabled in order to manage the problem with Deflate
module, E-Tag and HTTP Code 304  
# See : https://fullstackhack.wordpress.com/2014/12/10/the-pain-of-etags-
mod_deflate-apache-2-4-and-tomcat-7/  
# See :
http://httpd.apache.org/docs/trunk/mod/mod_deflate.html#deflatealteretag  
# The directive doesn't work in Ubuntu 15.10 with Apache 2.4.12  
RUN a2enmod request  
  
RUN composer install --prefer-dist --quiet --no-interaction --no-dev  
  
# Composer autoloader optimization  
RUN composer dump-autoload --optimize

