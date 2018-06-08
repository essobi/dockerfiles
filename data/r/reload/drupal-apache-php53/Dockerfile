FROM ubuntu:12.04  
MAINTAINER Mads H. Danquah <mads@danquah.dk>  
  
VOLUME ["/var/www"]  
  
RUN apt-get update && \  
apt-get install -y \  
apache2 \  
php5 \  
php5-cli \  
libapache2-mod-php5 \  
php5-gd \  
php5-mysql \  
php5-xdebug \  
php5-curl  
  
COPY vhost.conf /etc/apache2/sites-available/default  
COPY custom-php.ini /etc/php5/apache2/conf.d/  
COPY run /usr/local/bin/run  
RUN chmod +x /usr/local/bin/run  
RUN a2enmod rewrite  
  
EXPOSE 80  
CMD ["/usr/local/bin/run"]  

