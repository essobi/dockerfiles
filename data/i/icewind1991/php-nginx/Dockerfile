FROM php:5-fpm  
MAINTAINER Robin Appelman <robin@icewind.nl>  
  
RUN DEBIAN_FRONTEND=noninteractive ;\  
apt-get update && \  
apt-get install --assume-yes \  
bzip2 \  
nginx \  
libaio-dev \  
wget \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
# Oracle instantclient  
RUN wget https://github.com/icewind1991/php-nginx/raw/master/instantclient-
basic-linux.x64-12.1.0.2.0.zip -O /tmp/instantclient-basic-
linux.x64-12.1.0.2.0.zip \  
&& wget https://github.com/icewind1991/php-nginx/raw/master/instantclient-sdk-
linux.x64-12.1.0.2.0.zip -O /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip \  
&& wget https://github.com/icewind1991/php-nginx/raw/master/instantclient-
sqlplus-linux.x64-12.1.0.2.0.zip -O /tmp/instantclient-sqlplus-
linux.x64-12.1.0.2.0.zip \  
&& unzip /tmp/instantclient-basic-linux.x64-12.1.0.2.0.zip -d /usr/local/ \  
&& unzip /tmp/instantclient-sdk-linux.x64-12.1.0.2.0.zip -d /usr/local/ \  
&& unzip /tmp/instantclient-sqlplus-linux.x64-12.1.0.2.0.zip -d /usr/local/ \  
&& ln -s /usr/local/instantclient_12_1 /usr/local/instantclient \  
&& ln -s /usr/local/instantclient/libclntsh.so.12.1
/usr/local/instantclient/libclntsh.so \  
&& ln -s /usr/local/instantclient/sqlplus /usr/bin/sqlplus \  
&& rm /tmp/instantclient-*.zip \  
&& echo 'instantclient,/usr/local/instantclient' | pecl install oci8-2.0.10 \  
&& echo "extension=oci8.so" > $PHP_INI_DIR/conf.d/30-oci8.ini  
  
# php exceptions  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq5 \  
libpq-dev \  
libsqlite3-dev \  
libcurl4-openssl-dev \  
libicu-dev \  
&& docker-php-ext-install iconv mcrypt zip pdo pdo_pgsql pdo_sqlite pgsql
pdo_mysql intl curl mbstring \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& apt-get remove -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libpq-dev \  
libsqlite3-dev \  
libcurl4-openssl-dev \  
libicu-dev \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN pecl install apcu-4.0.10 \  
&& pecl install redis-2.2.8 \  
&& pecl install xdebug \  
&& export VERSION=`php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;"` \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/${VERSION} \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so `php -r "echo
ini_get('extension_dir');"`/blackfire.so \  
&& echo "extension=blackfire.so\nblackfire.agent_socket=\${BLACKFIRE_PORT}" >
$PHP_INI_DIR/conf.d/blackfire.ini \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> $PHP_INI_DIR/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=off" >> $PHP_INI_DIR/conf.d/xdebug.ini  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer  
  
ADD apcu.ini opcache.ini redis.ini $PHP_INI_DIR/conf.d/  
  
ADD nginx.conf nginx-app.conf /etc/nginx/  
  
ADD php-fpm.conf /usr/local/etc/  
ADD index.php /var/www/html/  
  
ADD bootstrap-nginx.sh /usr/local/bin/  
  
EXPOSE 80  
ENTRYPOINT ["bootstrap-nginx.sh"]  

