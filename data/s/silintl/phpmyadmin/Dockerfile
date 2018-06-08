FROM silintl/php-web:latest  
MAINTAINER "Phillip Shipley" <phillip_shipley@sil.org>  
  
ENV REFRESHED_AT 2015-08-10  
# Copy in vhost config  
COPY phpmyadmin-vhost.conf /etc/apache2/sites-enabled/  
  
# Create folder for phpmyadmin and install via composer  
RUN mkdir -p /data  
COPY composer.json /data/  
WORKDIR /data  
RUN composer install --prefer-dist --no-interaction --no-dev  
  
EXPOSE 80  
CMD ["apache2ctl", "-D", "FOREGROUND"]  

