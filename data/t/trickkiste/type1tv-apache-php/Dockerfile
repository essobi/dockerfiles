FROM ubuntu:trusty  
MAINTAINER mark@trickkiste.at  
  
EXPOSE 80  
## some stuff taken from docker-library/php ##  
RUN apt-get update && apt-get -y dist-upgrade && apt-get install -y
apache2-bin --no-install-recommends libapache2-mod-php5 php5-mysql php5-mcrypt
php5-imagick php5-imap php5-sqlite php5-pgsql php5-odbc php5-json php5-geoip
php5-memcache php5-memcached && rm -rf /var/lib/apt/lists/* && apt-get
autoclean && apt-get clean && apt-get autoremove  
  
RUN rm -rf /var/www/html && mkdir -p /var/lock/apache2 /var/run/apache2
/var/log/apache2 /var/www/html && chown -R www-data:www-data /var/lock/apache2
/var/run/apache2 /var/log/apache2 /var/www/html  
  
# Apache + PHP requires preforking Apache for best results  
RUN a2dismod mpm_event && a2enmod mpm_prefork && a2enmod rewrite  
  
RUN mv /etc/apache2/apache2.conf /etc/apache2/apache2.conf.dist  
COPY apache2.conf /etc/apache2/apache2.conf  
  
COPY apache2-foreground /usr/local/bin/  
WORKDIR /var/www/html  
  
CMD ["apache2-foreground"]  

