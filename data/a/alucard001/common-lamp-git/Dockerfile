FROM ubuntu:16.04  
MAINTAINER Ellery Leung <alucard001@gmail.com>  
  
# Webroot is in /var/www/html  
# Apache 2 config file is in /etc/apache2  
RUN apt-get update && \  
apt-get install -y php7* \  
php-redis \  
composer \  
apache2* \  
vim \  
python3 \  
libapache2-mod-php* \  
&& apt-get clean \  
&& apt-get autoclean  
  
RUN a2enmod rewrite  
RUN a2enmod expires  
RUN a2enmod headers  
  
# Allow website to use .htaccess  
RUN printf "<Directory \"/var/www/html/\">\n\tAllowOverride
All\n</Directory>\n" >> /etc/apache2/sites-available/000-default.conf  
  
RUN service apache2 stop  
  
WORKDIR /var/www/html  
  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]

