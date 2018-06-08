FROM gabrieltakacs/debian-jessie:1.0.1  
MAINTAINER Gabriel Takács <gtakacs@gtakacs.sk>  
  
# Copy and add files first (to make dockerhub autobuild working:
https://forums.docker.com/t/automated-docker-build-fails/22831/14)  
COPY run.sh /run.sh  
  
# Install Apache2, supervisor, PHP 5.6  
RUN apt-get update && \  
apt-get -y install \  
apache2 \  
supervisor \  
php5 \  
php5-pgsql \  
php5-mysql \  
php5-mcrypt \  
php5-gd \  
php5-curl \  
php5-json \  
php5-dev \  
php5-memcache \  
php5-memcached \  
php5-imagick \  
memcached \  
imagemagick \  
postfix  
  
# Install NPM & NPM modules (gulp, bower)  
RUN apt-get -y install nodejs-legacy nodejs npm  
RUN npm install -g \  
gulp \  
bower  
  
# php5-fpm configuration  
COPY ./php5/php.ini /etc/php5/apache2/php.ini  
  
# Install composer  
ENV COMPOSER_HOME=/composer  
RUN mkdir /composer \  
&& curl -sS https://getcomposer.org/download/1.2.1/composer.phar >
composer.phar  
  
RUN mkdir -p /opt/composer \  
&& mv composer.phar /usr/local/bin/composer \  
&& chmod 777 /usr/local/bin/composer  
  
# Configure xdebug  
#RUN echo 'zend_extension="/usr/lib/php7/modules/xdebug.so"' >>
/etc/php7/php.ini \  
# && echo "xdebug.remote_enable=on" >> /etc/php7/php.ini \  
# && echo "xdebug.remote_autostart=off" >> /etc/php7/php.ini \  
# && echo "xdebug.remote_connect_back=0" >> /etc/php7/php.ini \  
# && echo "xdebug.remote_port=9001" >> /etc/php7/php.ini \  
# && echo "xdebug.remote_handler=dbgp" >> /etc/php7/php.ini \  
# && echo "xdebug.remote_host=192.168.65.1" >> /etc/php7/php.ini  
# (Only for MAC users) Fill IP address from:  
# cat
/Users/gtakacs/Library/Containers/com.docker.docker/Data/database/com.docker.driver.amd64-linux/slirp/host  
# Source topic on Docker forums: https://forums.docker.com/t/ip-address-for-
xdebug/10460/22  
# Copy Supervisor config file  
COPY supervisor/supervisord.conf /etc/supervisor/conf.d/supervisord.conf  
  
RUN adduser --shell /sbin/nologin --disabled-login www-data www-data  
RUN chown -R www-data:www-data /run/apache2/  
  
# Copy Apache2 config  
RUN rm /etc/apache2/sites-available/000-default.conf  
RUN rm /etc/apache2/sites-enabled/000-default.conf  
COPY apache2/web.conf /etc/apache2/sites-available/000-default.conf  
RUN a2ensite 000-default  
RUN a2enmod rewrite  
  
# Make run file executable  
RUN chmod a+x /run.sh  
  
RUN chmod a+rw /var/log/apache2  
  
#RUN apk --no-cache --update add icu icu-libs icu-dev  
#RUN docker-php-ext-install intl  
EXPOSE 80 443 25  
CMD ["/run.sh"]  
WORKDIR /var/www/web  

