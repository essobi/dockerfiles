FROM nickistre/ubuntu-lamp:14.04  
MAINTAINER Nicholas Istre <nicholas.istre@e-hps.com>  
  
# Install xdebug for php debugging  
RUN apt-get install -y php5-xdebug  
ADD xdebug_settings.ini /etc/php5/mods-available/  
RUN php5enmod xdebug_settings  
  

