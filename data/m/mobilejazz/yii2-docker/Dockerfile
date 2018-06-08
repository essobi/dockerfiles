FROM ubuntu:16.04  
# Update  
RUN apt-get -y update  
RUN apt-get -y upgrade  
  
# Install supervisor  
RUN apt-get install -y supervisor  
  
# Install command line utils  
RUN apt-get install -y curl mcrypt git gawk wget vim sudo  
  
# Install nginx  
RUN apt-get install -y nginx  
RUN echo "daemon off;" >> /etc/nginx/nginx.conf  
  
# Install cron  
RUN apt-get install cron  
  
# Remove apache  
RUN apt-get purge apache2 -y  
  
# Purge php 5  
RUN apt-get purge php5-common -y  
  
# Install Imagemagick  
RUN apt-get install -y imagemagick  
  
# Install PHP 7 and some common extensions  
RUN apt-get install -y php php-imagick php-fpm php-mcrypt php-mysql php-gd
php-dev php-xdebug php-curl php-intl php-zip php-mbstring php-soap  
  
# Enable mcrypt  
RUN phpenmod mcrypt  
  
# Disable xdebug for composer and other cli invocations  
RUN phpdismod -s cli xdebug  
  
# php-fpm socket file will go in this directory  
RUN mkdir /var/run/php  
  
# Install PHP additional modules  
RUN apt-get install -y adminer  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
RUN chown www-data:www-data /usr/local/bin/composer  
  
# Setup xdebug  
ADD xdebug/xdebug.ini /etc/php/7.0/mods-available/xdebug.ini  
ADD xdebug/xdebug.mac.ini /etc/php/7.0/mods-available/xdebug.mac.ini  
ADD xdebug/xdebug.win.ini /etc/php/7.0/mods-available/xdebug.win.ini  
  
#  
RUN usermod -u 1000 www-data  
RUN chown -R www-data:www-data /var/www  
  
# FPM file upload config for larger file uploads  
ADD fpm/conf.d/20-fileupload.ini /etc/php/7.0/fpm/conf.d/20-fileupload.ini  
  
# Nginx configuration file  
RUN rm /etc/nginx/sites-available/default  
ADD nginx/sites-available/default /etc/nginx/sites-available/default  
  
# Supervisord configuration file  
ADD supervisord/nginx.conf /etc/supervisor/conf.d/nginx.conf  
ADD supervisord/fpm.conf /etc/supervisor/conf.d/fpm.conf  
  
# Run scripts  
ADD scripts/run.sh /run.sh  
ADD scripts/run-cron.sh /run-cron.sh  
ADD scripts/run-mac.sh /run-mac.sh  
ADD scripts/run-win.sh /run-win.sh  
ADD scripts/start-nginx.sh /start-nginx.sh  
ADD scripts/exec-www.sh /exec-www.sh  
  
RUN chmod 777 /run.sh  
RUN chmod 777 /run-cron.sh  
RUN chmod 777 /run-mac.sh  
RUN chmod 777 /run-win.sh  
RUN chmod 777 /start-nginx.sh  
RUN chmod 777 /exec-www.sh  
  
# Install some global composer dependencies  
RUN /exec-www.sh composer global require 'hirak/prestissimo:^0.3'  
  
# Data volumnes  
VOLUME '/var/www/html'  
  
# Ports  
EXPOSE 80 443  
# Start  
CMD ["/run.sh"]  

