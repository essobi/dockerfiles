FROM ubuntu:15.10  
RUN echo "Europe/Madrid" > /etc/timezone && \  
ln -s -f /usr/share/zoneinfo/Europe/Madrid /etc/localtime && \  
locale-gen es_ES.UTF-8 && \  
echo "deb http://ppa.launchpad.net/ondrej/php/ubuntu wily main" >>
/etc/apt/sources.list && \  
echo "deb-src http://ppa.launchpad.net/ondrej/php/ubuntu wily main" >>
/etc/apt/sources.list && \  
apt-key adv --keyserver keyserver.ubuntu.com --recv-keys E5267A6C && \  
apt-get -yqq update && \  
apt-get -yqq install zip vim curl git git-core apache2 libapache2-mod-php7.0
sqlite3 imagemagick wget \  
php7.0 php7.0-cli php7.0-pgsql php7.0-sqlite3 php7.0-intl php7.0-mcrypt
php7.0-curl \  
php7.0-gd php7.0-json php7.0-mbstring php7.0-xml \  
php-xdebug php-apcu php-apcu-bc php-imagick php-memcached && \  
a2enmod rewrite vhost_alias headers expires filter && \  
rm -fr /var/www/html  
  
RUN curl -sS https://getcomposer.org/installer | php &&\  
mv composer.phar /usr/local/bin/composer  
  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_RUN_DIR /var/run/apache2  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2/apache2.pid  
RUN mkdir -p $APACHE_RUN_DIR $APACHE_LOCK_DIR $APACHE_LOG_DIR  
RUN service apache2 stop  
EXPOSE 80  
CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]  

