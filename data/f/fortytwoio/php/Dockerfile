## Version 1.0.2  
FROM fortytwoio/base  
MAINTAINER Thomas Fritz <thomas.fritz@forty-two.io>  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qqy \  
php5-fpm \  
php-apc \  
php5-gd \  
php5-curl \  
php5-memcached \  
php5-mysqlnd \  
php5-pgsql \  
php5-mcrypt \  
php5-sqlite \  
php5-imagick \  
> /dev/null 2>&1  
  
ADD ./etc/php5/fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ADD ./etc/php5/fpm/php.ini /etc/php5/fpm/php.ini  
ADD ./etc/php5/fpm/pool.d/www.conf /etc/php5/fpm/pool.d/www.conf.tpl  
ADD ./info.php /srv/www/info.php  
  
ONBUILD ADD ./etc/php5/fpm/php-fpm.conf /etc/php5/fpm/php-fpm.conf  
ONBUILD ADD ./etc/php5/fpm/php.ini /etc/php5/fpm/php.ini  
ONBUILD ADD ./etc/php5/fpm/pool.d/ /etc/php5/fpm/pool.d/  
  
VOLUME "/srv/www/"  
EXPOSE 9000  

