FROM debian:jessie  
  
MAINTAINER Manghao  
  
EXPOSE 80  
RUN DEBIAN_FRONTEND=noninteractive apt-get install  
  
RUN \  
apt-get update && \  
apt-get install -y \  
curl \  
wget \  
git  
  
RUN echo "deb http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
echo "deb-src http://packages.dotdeb.org jessie all" >>
/etc/apt/sources.list.d/dotdeb.org.list && \  
wget -O- http://www.dotdeb.org/dotdeb.gpg | apt-key add -  
  
RUN \  
apt-get update && \  
apt-get install -y \  
apache2 \  
php7.0 \  
libapache2-mod-php7.0 \  
php7.0-mysql \  
php7.0-curl \  
php7.0-json \  
php7.0-gd \  
php7.0-mcrypt \  
php7.0-msgpack \  
php7.0-memcached \  
php7.0-intl \  
php7.0-sqlite3 \  
php7.0-gmp \  
php7.0-geoip \  
php7.0-mbstring \  
php7.0-xml \  
php7.0-zip \  
php7.0-cli \  
php7.0-pdo-odbc \  
php7.0-xdebug \  
nano  
  
RUN apt-get clean \  
&& rm -rf /var/lib/lists/*  
  
RUN a2enmod php7.0 \  
&& a2enmod rewrite \  
&& service apache2 restart  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN sed -i "s/error_reporting = .*$/error_reporting = E_ALL/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/display_errors = .*$/display_errors = On/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/display_startup_errors = .*$/display_startup_errors = On/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/log_errors = .*$/log_errors = On/" /etc/php/7.0/apache2/php.ini  
RUN sed -i "s/report_memleaks = .*$/report_memleaks = On/"
/etc/php/7.0/apache2/php.ini  
RUN sed -i "s/track_errors = .*$/track_errors = On/"
/etc/php/7.0/apache2/php.ini  
  
RUN rm -f /var/run/apache2.pid  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_GROUP www-data  
ENV APACHE_LOG_DIR /var/log/apache2  
ENV APACHE_LOCK_DIR /var/lock/apache2  
ENV APACHE_PID_FILE /var/run/apache2.pid  
ENV PHP_ERROR_REPORTING "E_ALL \& ~E_NOTICE \& ~E_STRICT \& ~E_DEPRECATED"  
ENV PATH "/root/.composer/vendor/bin:$PATH"  
VOLUME /var/www/html  
  
COPY ./var/www/html/* /var/www/html/  
ADD ./config/vhost.conf /etc/apache2/sites-enabled/000-default.conf  
ADD ./config/xdebug.ini ${PHP_INI_DIR}/conf.d/docker-php-pecl-
xdebug.ini.disabled  
  
RUN mkdir -p /app/public && chown -R www-data:www-data /app  
WORKDIR /app  
  
CMD ["/usr/sbin/apache2", "-D", "FOREGROUND"]  

