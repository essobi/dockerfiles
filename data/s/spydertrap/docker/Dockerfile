FROM debian:jessie  
  
RUN apt-get update \  
&& apt-get install -y \  
pdftk \  
apache2 \  
php5 \  
php5-curl \  
php5-json \  
php5-mysql \  
php5-pgsql \  
php5-gd \  
php5-mcrypt \  
php5-xdebug \  
&& rm -rf /var/lib/apt/lists/* \  
&& /usr/sbin/a2dismod 'mpm_*' \  
&& /usr/sbin/a2enmod mpm_prefork \  
&& /usr/sbin/a2enmod rewrite \  
&& /usr/sbin/a2enmod headers \  
&& mv /etc/apache2/sites-available/000-default.conf /etc/apache2/sites-
available/000-default.conf.bak  
  
COPY 000-default.conf /etc/apache2/sites-available/000-default.conf  
  
RUN find /etc/php5/ -type f -exec sed -i
's/post_max_size\s*=.*/post_max_size=80M/g' {} \;  
RUN find /etc/php5/ -type f -exec sed -i
's/upload_max_filesize\s*=.*/upload_max_filesize=80M/g' {} \;  
RUN echo 'xdebug.max_nesting_level=200' >> /etc/php5/mods-available/xdebug.ini  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

