ARG DOCKER_TAG  
FROM brumbrum/base:$DOCKER_TAG  
MAINTAINER Alessandro Lattao <alessandro.lattao@brumbrum.it>  
  
# Let the conatiner know that there is no tty  
ENV DEBIAN_FRONTEND noninteractive  
  
# Configuro rsyslog  
ADD bin/composer-setup.php /composer-setup.php  
  
RUN \  
apt-get -y --no-install-recommends install software-properties-common wget
gnupg2 debconf-utils && \  
echo 'deb http://apt.newrelic.com/debian/ newrelic non-free' | tee
/etc/apt/sources.list.d/newrelic.list && \  
wget -O- https://download.newrelic.com/548C16BF.gpg | apt-key add - && \  
apt-get update && \  
apt-get -y --no-install-recommends install ssh newrelic-php5 php7.0-fpm
php7.0-imap php-redis php7.0-xml php7.0-gd php7.0-soap php7.0-intl php-ssh2
php7.0-bcmath php7.0-mbstring php7.0-curl php7.0-mysql php7.0-zip rsyslog && \  
mkdir -p /var/run/php && \  
apt-get -y purge software-properties-common wget gnupg2 debconf-utils && \  
php /composer-setup.php --install-dir=/usr/bin --filename=composer \  
apt-get -y autoclean && \  
apt-get -y clean && \  
apt-get -y autoremove  
  
# Configuro la timezone in PHP.INI  
RUN sed -i -e "s/;date.timezone =/date.timezone = Europe\/Rome/g"
/etc/php/7.0/fpm/php.ini  
  
# Configuro rsyslog  
ADD etc/rsyslog.conf /etc/rsyslog.conf  
ADD etc/rsyslog.d/50-default.conf /etc/rsyslog.d/50-default.conf  
  
# configure php-fpm  
RUN rm /etc/php/7.0/fpm/pool.d/www.conf  
ADD /etc/php/7.0/fpm/pool.d/www.conf /etc/php/7.0/fpm/pool.d/www.conf  
RUN touch /var/log/php7.0-app.log && chown www-data:www-data
/var/log/php7.0-app.log && chmod 664 /var/log/php7.0-app.log  
  
ADD bin/entrypoint.sh /entrypoint.sh  
RUN ["chmod", "+x", "/entrypoint.sh"]  
ENTRYPOINT ["/entrypoint.sh"]  

