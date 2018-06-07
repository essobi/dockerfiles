FROM php:5.6.32-apache-jessie  
RUN a2dissite 000-default.conf  
RUN a2enmod rewrite  
RUN echo "ServerName express.live" | tee /etc/apache2/conf-
available/servername.conf \  
&& a2enconf servername  
#RUN ./etc/apache2/envvars  
RUN apt-get update -y \  
&& apt-get upgrade -y \  
&& apt-get install -y php5-gd php5-mysql php5-memcached memcached curl
php5-cli bzip2 gettext \  
&& apt-get install -y php5-dev apache2-prefork-dev build-essential \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> /usr/local/etc/php/conf.d/xdebug.ini  
  
RUN a2enmod expires  
RUN apachectl restart

