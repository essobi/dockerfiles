FROM php:apache  
  
MAINTAINER Doosik Kim <doosik71@gmail.com>  
  
LABEL description="apache, php, laravel"  
  
RUN apt-get update && \  
apt-get -y install apt-utils && \  
apt-get -y install git php5-mcrypt php5-json zip unzip php-pclzip && \  
apt-get -y autoremove && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
RUN /usr/sbin/a2enmod rewrite  
  
ADD 000-laravel.conf /etc/apache2/sites-available/  
  
RUN /usr/sbin/a2dissite '*' && \  
/usr/sbin/a2ensite 000-laravel  
  
RUN /usr/bin/curl -sS https://getcomposer.org/installer | /usr/local/bin/php  
  
RUN /bin/mv composer.phar /usr/local/bin/composer  
  
RUN /usr/local/bin/composer create-project laravel/laravel /var/www/laravel
--prefer-dist  
  
RUN /bin/chown www-data:www-data -R /var/www/laravel  
  
EXPOSE 80 443  
WORKDIR /home  
  
VOLUME ["/home"]  
  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

