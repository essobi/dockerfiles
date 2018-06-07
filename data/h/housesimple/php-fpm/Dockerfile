#  
# PHP-FPM Dockerfile  
#  
# https://bitbucket.org/housesimple/docker-php-fpm  
#  
FROM housesimple/centos  
  
MAINTAINER Olly Nevard <olly.nevard@housesimple.com>  
  
# Install IUS repository, PHP 5.6 and required PHP modules.  
RUN yum -y install
https://dl.iuscommunity.org/pub/ius/stable/CentOS/7/x86_64/ius-
release-1.0-14.ius.centos7.noarch.rpm && \  
yum -y install \  
php56u \  
php56u-common \  
php56u-fpm \  
php56u-gd \  
php56u-intl \  
php56u-mbstring \  
php56u-mysqlnd \  
php56u-pdo \  
php56u-pear \  
php56u-pecl-xdebug \  
php56u-process \  
php56u-suhosin \  
php56u-xml && \  
yum clean all  
  
# Add PHP config.  
ADD php-fpm.conf /etc/php-fpm.conf  
  
# Define mountable directories.  
VOLUME ["/etc/php-fpm.d", "/var/log/php-fpm", "/srv/http"]  
  
# Define entrypoint.  
ENTRYPOINT ["php-fpm"]  
  
# Expose ports.  
EXPOSE 9000  

