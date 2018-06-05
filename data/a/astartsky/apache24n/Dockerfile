FROM ubuntu:14.04  
MAINTAINER Dmitry Sinev <astartsky@gmail.com>  
  
ENV DEBIAN_FRONTEND=noninteractive \  
TERM=xterm  
  
# install custom repositories for php5.5, apache2.4  
RUN apt-key adv --keyserver keyserver.ubuntu.com --recv-key E5267A6C  
RUN apt-get update && apt-get install -y software-properties-common && \  
add-apt-repository -y ppa:ondrej/php5-5.6 && \  
add-apt-repository ppa:ondrej/apache2  
  
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
nano \  
wget \  
build-essential  
  
# install node.js  
RUN curl -sL https://deb.nodesource.com/setup_5.x | bash -  
RUN apt-get update && apt-get install -y nodejs && npm install -g npm@3  
  
# configure apache2  
RUN rm /etc/apache2/sites-enabled/000-default.conf && \  
rm -rf /var/www/html && \  
a2enmod -f rewrite && \  
a2enmod -f headers && \  
a2enmod -f deflate && \  
a2enmod -f expires && \  
a2enmod -f http2 && \  
a2enmod -f ssl  
  
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
RUN touch /var/log/cron.log && \  
echo '* * * * * root /cron.sh >> /var/log/cron.log 2>&1' >> /etc/crontab && \  
echo '/bin/su - www-data -s /bin/sh -c "source /env.sh; /usr/bin/php
/var/www/console.php cron:run"' >> /cron.sh  
  
RUN chmod +x /cron.sh  
RUN rm /bin/sh && ln -s /bin/bash /bin/sh  
  
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
  
# install modspeed  
RUN wget -P ~/ https://dl-ssl.google.com/dl/linux/direct/mod-pagespeed-
stable_current_amd64.deb && \  
dpkg -i ~/mod-pagespeed-stable_current_amd64.deb && \  
rm ~/mod-pagespeed-stable_current_amd64.deb  
  
# cleanup  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www  
  
EXPOSE 80  
EXPOSE 443  
CMD ["/usr/bin/supervisord"]  
  

