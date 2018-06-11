FROM wizjostudio/ubuntu:latest  
MAINTAINER Piotr Rzeczkowski <piotr@rzeka.net>  
  
RUN apt-key adv --keyserver keyserver.ubuntu.com \--recv-keys 4F4EA0AAE5267A6C
&& \  
LC_ALL=C.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get update && \  
apt-get install -y \  
php5.6-fpm \  
php5.6-json \  
php5.6-curl \  
php5.6-gd \  
php-imagick \  
php5.6-intl \  
php5.6-mcrypt \  
php-memcached \  
php-redis \  
php5.6-mysql \  
php5.6-xml \  
php5.6-mbstring \  
php5.6-soap \  
php-xdebug && \  
phpdismod -v 5.6 xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
RUN mkdir /run/php  
  
RUN sed -i -e "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/g"
/etc/php/5.6/fpm/php.ini && \  
sed -i -e "s/upload_max_filesize\s*=\s*2M/upload_max_filesize = 100M/g"
/etc/php/5.6/fpm/php.ini && \  
sed -i -e "s/post_max_size\s*=\s*8M/post_max_size = 100M/g"
/etc/php/5.6/fpm/php.ini && \  
sed -i -e "s/;daemonize\s*=\s*yes/daemonize = no/g" /etc/php/5.6/fpm/php-
fpm.conf && \  
sed -i -e "s/;catch_workers_output\s*=\s*yes/catch_workers_output = yes/g"
/etc/php/5.6/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_children = 5/pm.max_children = 9/g"
/etc/php/5.6/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.start_servers = 2/pm.start_servers = 3/g"
/etc/php/5.6/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.min_spare_servers = 1/pm.min_spare_servers = 2/g"
/etc/php/5.6/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_spare_servers = 3/pm.max_spare_servers = 4/g"
/etc/php/5.6/fpm/pool.d/www.conf && \  
sed -i -e "s/pm.max_requests = 500/pm.max_requests = 100/g"
/etc/php/5.6/fpm/pool.d/www.conf && \  
sed -i -e "s/listen\s*=\s*\/run\/php\/php5.6-fpm.sock/listen = 9000/g"
/etc/php/5.6/fpm/pool.d/www.conf  
  
CMD ["php-fpm5.6", "-F"]  
  
EXPOSE 9000  

