FROM weyforth/wordpress-base  
  
MAINTAINER "Mike Farrow" <contact@mikefarrow.co.uk>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update -y && \  
apt-get install -y software-properties-common  
  
RUN apt-add-repository ppa:ondrej/php5-5.6 && \  
apt-get update -y && sudo apt-get upgrade -y --force-yes  
# Install PHP-FPM and popular/wordpress required extensions  
RUN apt-get install -y --force-yes \  
php5-fpm \  
php5-curl \  
php5-gd \  
php5-geoip \  
php5-imagick \  
php5-imap \  
php5-json \  
php5-ldap \  
php5-mcrypt \  
php5-memcache \  
php5-memcached \  
php5-mongo \  
php5-mssql \  
php5-mysqlnd \  
php5-redis \  
php5-sqlite \  
php5-xmlrpc \  
php5-xcache && \  
php5enmod mcrypt && \  
service php5-fpm restart  
  
# Configure PHP-FPM  
RUN sed -i "s/;date.timezone =.*/date.timezone = UTC/" /etc/php5/fpm/php.ini
&& \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php5/fpm/php.ini && \  
sed -i "s/display_errors = Off/display_errors = stderr/" /etc/php5/fpm/php.ini
&& \  
sed -i "s/upload_max_filesize = 2M/upload_max_filesize = 30M/"
/etc/php5/fpm/php.ini && \  
sed -i "s/;opcache.enable=0/opcache.enable=0/" /etc/php5/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php5/fpm/php-fpm.conf
&& \  
sed -i '/^listen = /clisten = 9000' /etc/php5/fpm/pool.d/www.conf && \  
sed -i '/^listen.allowed_clients/c;listen.allowed_clients ='
/etc/php5/fpm/pool.d/www.conf && \  
sed -i '/^;catch_workers_output/ccatch_workers_output = yes'
/etc/php5/fpm/pool.d/www.conf && \  
sed -i '/^;env\\[TEMP\\] = .*/aclear_env = No' /etc/php5/fpm/pool.d/www.conf  
  
EXPOSE 9000  
  
ENTRYPOINT ["/usr/sbin/php5-fpm", "-F"]  

