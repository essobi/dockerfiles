FROM centos:7  
RUN yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm  
RUN yum -y install http://rpms.remirepo.net/enterprise/remi-release-7.rpm  
RUN yum -y install yum-utils  
  
RUN yum -y install php70-php-cli \  
php70-php-fpm \  
php70-php-bcmath \  
php70-php-gd \  
php70-php-gmp \  
php70-php-intl \  
php70-php-mbstring \  
php70-php-mcrypt \  
php70-php-pdo \  
php70-php-mysqlnd \  
php70-php-pecl-crypto \  
php70-php-pecl-geoip \  
php70-php-pecl-imagick \  
php70-php-pecl-memcache \  
php70-php-pecl-memcached \  
php70-php-pecl-mongodb \  
php70-php-pecl-ssh2 \  
php70-php-pecl-xdebug \  
php70-php-soap \  
php70-php-xml \  
php70-php-opcache \  
php70-php-pecl-redis  
  
WORKDIR /share  
  
ADD etc/php7/php-fpm.d/*.conf /etc/opt/remi/php70/php-fpm.d/  
ADD etc/php7/php.d/*.ini /etc/opt/remi/php70/php.d/  
  
EXPOSE 9000  
CMD ["/opt/remi/php70/root/usr/sbin/php-fpm", "-F"]  

