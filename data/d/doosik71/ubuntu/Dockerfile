FROM doosik71/ubuntu:apm  
  
MAINTAINER Doosik Kim <doosik71@gmail.com>  
  
LABEL description="Ubuntu 16.04, Apache 2.4, PHP 7.0, MySQL 5.7, laravel"  
  
ADD 000-laravel.conf /etc/apache2/sites-available/  
  
RUN /usr/sbin/a2dissite '*' && \  
/usr/sbin/a2ensite 000-laravel  
  
RUN /usr/local/bin/composer create-project laravel/laravel /var/www/laravel
--prefer-dist  
  
WORKDIR /var/www/laravel  
  
RUN /bin/chown www-data:www-data -R /var/www/laravel  
  
# Set port and volume.  
VOLUME /var/www/laravel  
  
# Start server.  
CMD /root/start_server.sh

