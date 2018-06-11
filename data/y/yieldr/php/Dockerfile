FROM php:7.2-apache-stretch  
  
# enable apache rewrite engine  
RUN set -x \  
&& a2enmod rewrite \  
&& a2enmod remoteip  
  
# install extensions  
RUN set -x \  
&& apt-get update \  
&& apt-get install -y --no-install-recommends \  
git \  
libmemcached-dev \  
zlib1g-dev \  
libpq-dev \  
libxml2-dev \  
# Install unzip  
&& apt-get install unzip \  
# install grpc  
&& apt-get install -y g++ make \  
&& pecl install grpc-1.9.0 \  
&& pecl install apcu-5.1.5 \  
# memcached for php7 must be installed from source  
&& docker-php-source extract \  
&& git clone --branch php7 https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached/ \  
# install pdo drivers, soap and mysqli  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install \  
zip \  
soap \  
memcached \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
opcache \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug apcu \  
&& docker-php-source delete \  
&& apt-get clean  
  
# prepare code folder and install crond  
RUN mkdir -p /home/code \  
&& ln -sf /home/code/web /var/www/code \  
&& chown www-data:www-data -R /home/code \  
&& usermod -u 1000 www-data  
  
ENV CRON_VERSION 0.8.0  
ENV CRON_OS linux  
ENV CRON_ARCH amd64  
  
RUN curl -o /usr/bin/crond -sSL
https://github.com/alexkappa/crond/releases/download/v$CRON_VERSION/crond-$CRON_OS-$CRON_ARCH
\  
&& chmod +x /usr/bin/crond \  
&& curl -sSL http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar -o php-cs-
fixer \  
&& chmod a+x php-cs-fixer \  
&& mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
COPY php.ini /usr/local/etc/php/  
  
COPY vhost.conf /etc/apache2/sites-available/000-default.conf  
  
ADD docker-entrypoint.sh /  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  
  
EXPOSE 80  
  
CMD ["apachectl", "-D", "FOREGROUND"]  

