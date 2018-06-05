FROM webdevops/php-nginx-dev:7.1  
MAINTAINER Alexander Garzon <agarzon@php.net>  
  
RUN apt-get update  
  
# ioncube for PHP 7.1  
ADD
https://downloads.ioncube.com/loader_downloads/ioncube_loaders_lin_x86-64.tar.gz
/tmp/  
RUN cd /tmp/ && tar xvfz /tmp/ioncube_loaders_lin_x86-64.tar.gz  
RUN cp /tmp/ioncube/ioncube_loader_lin_* /usr/local/lib/php/extensions/no-
debug-non-zts-20160303/  
RUN echo "zend_extension = /usr/local/lib/php/extensions/no-debug-non-
zts-20160303/ioncube_loader_lin_7.1.so" >
/usr/local/etc/php/conf.d/01-ioncube.ini  
RUN echo "zend_extension = /usr/local/lib/php/extensions/no-debug-non-
zts-20160303/ioncube_loader_lin_7.1.so" >
/usr/local/etc/php/conf.d/01-ioncube.ini  
RUN rm -rf /tmp/ioncube/  
  
# PHPUNIT  
ADD https://phar.phpunit.de/phpunit.phar /usr/local/bin/phpunit  
RUN chmod +x /usr/local/bin/phpunit  
  
# Install missing modules  
RUN apt-get install -y \  
libxml2-dev \  
&& docker-php-ext-install wddx \  
&& docker-php-ext-install xmlrpc  
  
# Intl  
RUN apt-get install -y libicu-dev  
RUN docker-php-ext-install intl  
  
# Memcached  
RUN apt-get install -y libmemcached-dev zlib1g-dev  
RUN pecl install memcached  
RUN docker-php-ext-enable memcached  
  
# ldap  
RUN apt-get install libldap2-dev -y && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap  
  
# clear  
RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

