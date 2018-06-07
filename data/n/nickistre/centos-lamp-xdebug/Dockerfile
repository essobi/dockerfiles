FROM nickistre/centos-lamp:6.6  
MAINTAINER Nicholas Istre <nicholas.istre@e-hps.com>  
  
# Install xdebug for php debugging  
RUN yum install -y php-pecl-xdebug  
ADD xdebug_settings.ini /etc/php.d/  
  

