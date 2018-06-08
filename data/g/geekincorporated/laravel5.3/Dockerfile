FROM eboraas/apache-php  
MAINTAINER Ed Boraas <ed@boraas.ca>  
  
RUN apt-get update && apt-get -y install git curl php5-mcrypt php5-json &&
apt-get -y autoremove && apt-get clean && rm -rf /var/lib/apt/lists/*  
  
RUN /usr/sbin/a2enmod rewrite  
  
ADD conf/apache/000-laravel.conf /etc/apache2/sites-available/  
ADD conf/apache/001-laravel-ssl.conf /etc/apache2/sites-available/  
RUN /usr/sbin/a2dissite '*' && /usr/sbin/a2ensite 000-laravel 001-laravel-ssl  
  
ENV LARAVEL_VERSION ~5.3.0  
RUN /usr/bin/curl -sS https://getcomposer.org/installer |/usr/bin/php  
RUN /bin/mv composer.phar /usr/local/bin/composer  
RUN /usr/local/bin/composer create-project laravel/laravel /var/www/laravel
$LARAVEL_VERSION \--prefer-dist --no-interaction && \  
php /var/www/laravel/artisan key:generate  
RUN /bin/chown www-data:www-data -R /var/www/laravel/storage
/var/www/laravel/bootstrap/cache  
  
WORKDIR /var/www/laravel/config/  
RUN mv database.php database.php.bak  
ADD conf/laravel/database.php database.php  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

