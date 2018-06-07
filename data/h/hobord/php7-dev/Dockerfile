FROM ubuntu:16.04  
MAINTAINER Balazs Szabo <balazs.szabo@gmail.com>  
  
RUN DEBIAN_FRONTEND=noninteractive && apt-get update && apt-get install -y \  
apache2 \  
curl \  
git \  
libapache2-mod-php \  
mcrypt \  
freetds-common \  
libsybdb5 \  
php \  
php-bz2 \  
php-cli \  
php-curl \  
php-date \  
php-db \  
php-dom \  
php-gd \  
php-intl \  
php-imap \  
php-json \  
php-ldap \  
php-odbc \  
php-pgsql \  
php-mbstring \  
php-mcrypt \  
php-mdb2 \  
php-mongodb \  
php-mysql \  
php-uuid \  
php-redis \  
php-sybase \  
php-sqlite3 \  
php-xdebug \  
php-zip \  
vim \  
&& a2enmod php7.0 \  
&& a2enmod rewrite \  
&& sed -i "s/short_open_tag = Off/short_open_tag = On/"
/etc/php/7.0/apache2/php.ini \  
&& sed -i "s/zend_extension/;zend_extension/"
/etc/php/7.0/cli/conf.d/20-xdebug.ini \  
&& apt-get clean \  
&& apt-get autoremove \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer 2>/dev/null 1>/dev/null  
#RUN php -r "copy('http://getcomposer.org/installer', 'composer-setup.php');"  
#RUN php composer-setup.php && mv composer.phar /usr/local/bin/composer && rm
composer-setup.php  
#RUN /usr/local/bin/composer self-update  
#ENV APACHE_RUN_USER www-data  
#ENV APACHE_RUN_GROUP www-data  
#ENV APACHE_LOG_DIR /var/log/apache2  
#ENV APACHE_LOCK_DIR /var/lock/apache2  
#ENV APACHE_PID_FILE /var/run/apache2.pid  
  
ADD 000-default.conf /etc/apache2/sites-available/  
ADD run.sh /  
RUN chmod +x /run.sh  
  
RUN usermod -u 1000 www-data \  
&& mkdir -p /var/www/public \  
&& chown -R www-data:www-data /var/www  
  
EXPOSE 80  
ENTRYPOINT ["bash"]  
VOLUME ["/var/www", "/var/www/public"]  
  
CMD ["/run.sh"]  

