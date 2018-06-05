FROM ubuntu:12.04  
MAINTAINER Dmitry Sinev <astartsky@gmail.com>  
ENV DEBIAN_FRONTEND=noninteractive \  
REFRESHED_AT=2015-09-03 \  
TERM=xterm  
  
# set locale  
RUN dpkg-reconfigure locales && \  
locale-gen ru_RU.UTF-8 && \  
/usr/sbin/update-locale LANG=ru_RU.UTF-8  
  
# install custom repositories  
RUN apt-get update && apt-get install -y python-software-properties && \  
add-apt-repository -y ppa:ondrej/php5-oldstable && \  
add-apt-repository ppa:chris-lea/node.js  
  
# install packages  
RUN apt-get update && apt-get install -y \  
apache2 \  
curl \  
libapache2-mod-php5 \  
php5-mysql \  
php5-gd \  
php5-curl \  
php-pear \  
php-apc \  
php5-mcrypt \  
php5-imagick \  
php5-memcache \  
php5-memcached \  
git \  
supervisor \  
cron \  
nodejs \  
nano  
  
# install uglify js  
RUN npm cache clean && \  
npm install --global uglify-js  
  
# configure apache2  
RUN mkdir /var/run/apache2 && \  
rm /etc/apache2/sites-enabled/000-default && \  
a2enmod rewrite && \  
a2enmod headers && \  
a2dismod deflate  
  
ENV APACHE_RUN_USER=www-data \  
APACHE_RUN_GROUP=www-data \  
APACHE_LOG_DIR=/var/log/apache2 \  
APACHE_PID_FILE=/var/run/apache2.pid \  
APACHE_RUN_DIR=/var/run/apache2 \  
APACHE_LOCK_DIR=/var/lock/apache2 \  
APACHE_SERVERADMIN=admin@localhost \  
APACHE_SERVERNAME=localhost \  
APACHE_SERVERALIAS=docker.localhost \  
APACHE_DOCUMENTROOT=/var/www  
  
# configure composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer && \  
chmod +x /usr/local/bin/composer  
  
# configure supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# configure php  
RUN sed -ri 's/^short_open_tag\s*=\s*Off/short_open_tag = On/g'
/etc/php5/cli/php.ini  
RUN sed -ri 's/^short_open_tag\s*=\s*Off/short_open_tag = On/g'
/etc/php5/apache2/php.ini  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php5/apache2/php.ini  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php5/cli/php.ini  
RUN sed -ri 's/^error_reporting\s*=.*$/error_reporting = E_ALL \&
~E_DEPRECATED \& ~E_NOTICE/g' /etc/php5/apache2/php.ini  
RUN sed -ri 's/^error_reporting\s*=.*$/error_reporting = E_ALL \&
~E_DEPRECATED \& ~E_NOTICE/g' /etc/php5/cli/php.ini  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
VOLUME ["/var/www"]  
WORKDIR /var/www  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

