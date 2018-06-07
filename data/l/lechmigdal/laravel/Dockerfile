FROM php:5-apache  
  
RUN apt-get update && \  
apt-get -y install git zip unzip php5-mcrypt php5-json && \  
php5enmod mcrypt && \  
php5enmod json && \  
a2enmod rewrite && \  
service apache2 restart && \  
cd /tmp && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar /usr/local/bin/composer && \  
composer global require "laravel/installer" && \  
export PATH=$PATH:$HOME/.composer/vendor/bin  
ADD https://raw.githubusercontent.com/lechmigdal/laravel-
docker/master/000-laravel.conf /etc/apache2/sites-available/  
ADD https://raw.githubusercontent.com/lechmigdal/laravel-
docker/master/001-laravel-ssl.conf /etc/apache2/sites-available/  
  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-laravel 001-laravel-ssl  
  
RUN /usr/local/bin/composer create-project laravel/laravel /var/www/laravel
\--prefer-dist  
  
# Below are app copying commands. Uncomment them depending on your needs. They
assume Dockerfile is stored in the laravel folder.  
#COPY app/ /var/www/laravel/app/  
#COPY public/ /var/www/laravel/public/  
#COPY bootstrap/ /var/www/laravel/bootstrap/  
#COPY config/ /var/www/laravel/config/  
#COPY resources/ /var/www/laravel/resources/  
#COPY routes/ /var/www/laravel/routes/  
#COPY storage/ /var/www/laravel/storage/  
#COPY composer.json /var/www/laravel/composer.json  
# End of app copying commands  
  
RUN /usr/local/bin/composer update \--working-dir /var/www/laravel  
  
RUN service apache2 restart  
  
RUN /bin/chown www-data:www-data -R /var/www/laravel/storage
/var/www/laravel/bootstrap/cache  
  
EXPOSE 80  
EXPOSE 443  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

