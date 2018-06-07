############################################################  
# Dockerfile to build CentOS,Nginx installed Container  
# Based on CentOS  
############################################################  
  
# Set the base image to Ubuntu  
FROM ideato/centos7_base  
  
# File Author / Maintainer  
MAINTAINER Alessandro Mazzoli <am@ideato.it>  
  
ONBUILD RUN yum -y update  
  
# Add the nginx and PHP dependent repository  
ADD nginx.repo /etc/yum.repos.d/nginx.repo  
  
# Installing PHP nginx supervisor  
RUN yum -y --enablerepo=remi,remi-php70 install nginx \  
php-fpm \  
php-common \  
php-cli \  
php-curl \  
php-bcmath \  
php-gd \  
php-intl \  
php-json \  
php-mbstring \  
php-mcrypt \  
php-mysqlnd \  
php-opcache \  
php-pdo \  
php-xml \  
php-xmlrpc \  
php-pecl-imagick \  
php-pecl-memcache \  
supervisor  
  
# Installing Composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Installing Idephix  
RUN curl http://getidephix.com/idephix.phar > /usr/local/bin/idx  
RUN chmod +x /usr/local/bin/idx  
  
  
# Adding the configuration file for Supervisor  
ADD supervisord.conf /etc/  
  
# Add folder & permission to www  
RUN useradd ideato  
RUN mkdir -p /var/www/vhosts  
RUN chown -R ideato:nginx /var/www/vhosts  
  
# Add folder & permission for sessions  
RUN mkdir -p /var/www/sessions  
RUN chown -R ideato:nginx /var/www/sessions  
  
# Set the port to 80  
EXPOSE 80  
  
# Executing supervisord  
CMD ["supervisord", "-n"]  

