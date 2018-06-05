# CHOSING DEBIAN  
FROM debian:8  
MAINTAINER Tim Tegeler <tegeler@creios.net>  
  
## SETTING ENVIRONMENT  
ENV ENVIRONMENT docker-dev  
  
## FIX FOR GETTING DNS FAILURES  
RUN echo "8.8.8.8" > /etc/resolv.conf  
RUN echo "8.8.4.4" >> /etc/resolv.conf  
  
# APT-GET  
RUN apt-get -qq update  
RUN apt-get -qq install -y rsync  
RUN apt-get -qq install -y vim  
RUN apt-get -qq install -y git  
  
## SUPERVISOR  
RUN apt-get install -y supervisor  
RUN mkdir -p /var/lock/apache2 /var/run/apache2  
ADD ./supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
## APACHE  
RUN apt-get install -y apache2  
ADD ./000-default.conf /etc/apache2/sites-available/000-default.conf  
RUN echo 'ServerName localhost' >> /etc/apache2/apache2.conf  
RUN a2ensite 000-default  
RUN a2enmod rewrite  
  
## PHP  
RUN apt-get install -y php5  
RUN apt-get install -y php5-mysql  
RUN apt-get install -y php5-imagick  
RUN apt-get install -y php5-gd  
RUN apt-get -qq install -y php5-mcrypt  
RUN sed -i "s/error_reporting = E_ALL & ~E_DEPRECATED &
~E_STRICT/error_reporting = E_ALL/" /etc/php5/apache2/php.ini  
RUN sed -i "s/display_errors = Off/display_errors = On/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/display_startup_errors = Off/display_startup_errors = On/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/post_max_size = 8M/post_max_size = 100M/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 100M/"
/etc/php5/apache2/php.ini  
RUN sed -i "s/;always_populate_raw_post_data =
-1/always_populate_raw_post_data = -1/" /etc/php5/apache2/php.ini  
  
## COMPOSER  
RUN php -r "readfile('http://getcomposer.org/composer.phar');" >
/usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
EXPOSE 80  
WORKDIR /root  
CMD ["/usr/bin/supervisord"]  

