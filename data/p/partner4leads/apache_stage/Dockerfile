FROM ubuntu:12.04  
MAINTAINER Dmitry Sinev <astartsky@gmail.com>  
ENV DEBIAN_FRONTEND=noninteractive \  
REFRESHED_AT=2015-08-27 \  
TERM=xterm  
  
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
php5-xdebug \  
git \  
cron \  
supervisor \  
nano  
  
# configure apache2  
RUN rm /etc/apache2/sites-enabled/000-default && \  
rm /var/www/index.html && \  
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
RUN mv composer.phar /usr/local/bin/composer  
RUN chmod +x /usr/local/bin/composer  
  
# configure crontab  
RUN touch /var/log/cron.log  
RUN echo "* * * * * root /usr/bin/php /var/www/cron.php >> /var/log/cron.log
2>&1" >> /etc/crontab  
  
# configure supervisor  
ADD supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
# configure php  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php5/apache2/php.ini  
RUN sed -ri 's/^display_errors\s*=\s*Off/display_errors = On/g'
/etc/php5/cli/php.ini  
RUN sed -ri 's/^short_open_tag\s*=\s*Off/short_open_tag = On/g'
/etc/php5/cli/php.ini  
RUN sed -ri 's/^short_open_tag\s*=\s*Off/short_open_tag = On/g'
/etc/php5/apache2/php.ini  
RUN sed -ri 's/^error_reporting\s*=.*$/error_reporting = E_ALL \&
~E_DEPRECATED \& ~E_NOTICE/g' /etc/php5/apache2/php.ini  
RUN sed -ri 's/^error_reporting\s*=.*$/error_reporting = E_ALL \&
~E_DEPRECATED \& ~E_NOTICE/g' /etc/php5/cli/php.ini  
RUN sed -i -e "s/.*sendmail_path =.*/sendmail_path = \/usr\/bin\/env
\/usr\/local\/bin\/catchmail --smtp-ip mc -f address@example\\.com/"
/etc/php5/apache2/php.ini  
RUN sed -i -e "s/.*sendmail_path =.*/sendmail_path = \/usr\/bin\/env
\/usr\/local\/bin\/catchmail --smtp-ip mc -f address@example\\.com/"
/etc/php5/cli/php.ini  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
EXPOSE 80  
CMD ["/usr/bin/supervisord"]  

