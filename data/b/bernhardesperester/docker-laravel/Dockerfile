FROM bernhardesperester/docker-apache-php:latest  
  
# File Author / Maintainer  
MAINTAINER Bernhard Esperester <bernhard@esperester.de>  
  
# install laravel / composer support  
RUN apt-get update && apt-get -y install php-curl php-zip php-gd php-mbstring
git && apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
# add config  
ADD 000-laravel.conf /etc/apache2/sites-available/  
ADD 001-laravel-ssl.conf /etc/apache2/sites-available/  
  
# disable / enable sites  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-laravel 001-laravel-ssl  
  
# install composer  
RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  
  
# install laravel  
# RUN /usr/local/bin/composer create-project laravel/laravel /var/www/laravel
--prefer-dist  
# RUN /bin/chown www-data:www-data -R /var/www/laravel/storage
/var/www/laravel/bootstrap/cache  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

