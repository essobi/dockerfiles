FROM php:7.1-apache  
  
RUN apt-get update \  
&& apt-get install -y \  
git \  
freetds-bin \  
freetds-dev \  
freetds-common \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
zlib1g-dev \  
libsybdb5 \  
libpq-dev \  
libjpeg-dev \  
libssl-dev \  
libmcrypt-dev \  
libpng12-dev \  
libz-dev \  
libmemcached-dev \  
python-software-properties \  
build-essential \  
&& ln -s /usr/lib/x86_64-linux-gnu/libsybdb.a /usr/lib/ \  
&& pecl install mongodb \  
&& echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/ext-mongo.ini \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install exif \  
&& docker-php-ext-install mbstring \  
&& docker-php-ext-install pdo_pgsql \  
&& docker-php-ext-install pdo_dblib \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install bcmath \  
&& docker-php-ext-install opcache \  
&& a2enmod rewrite \  
&& sed -i 's!/var/www/html!/var/www/public!g' /etc/apache2/apache2.conf \  
&& sed -i 's!/var/www/html!/var/www/public!g' /etc/apache2/sites-
available/000-default.conf \  
&& sed -i 's!/var/www/html!/var/www/public!g' /etc/apache2/sites-
available/default-ssl.conf \  
&& curl -sS https://getcomposer.org/installer \  
| php -- --install-dir=/usr/local/bin --filename=composer  
RUN { \  
echo 'date.timezone=UTC'; \  
echo 'display_errors=Off'; \  
echo 'log_errors=On'; \  
echo 'memory_limit = 1G'; \  
echo 'upload_max_filesize = 2048M'; \  
echo 'post_max_size = 2048M'; \  
} > /usr/local/etc/php/conf.d/laravel.ini  
  
RUN yes | pecl install xdebug \  
&& echo "zend_extension=$(find /usr/local/lib/php/extensions/ -name
xdebug.so)" > /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.idekey = PHPSTORM" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.default_enable = 1" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable = 1" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart = 1" >> /usr/local/etc/php/conf.d/xdebug.ini
\  
&& echo "xdebug.remote_connect_back = 1" >>
/usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.profiler_enable = 0" >> /usr/local/etc/php/conf.d/xdebug.ini \  
&& echo "xdebug.remote_host = dockerhost" >>
/usr/local/etc/php/conf.d/xdebug.ini  
  
# Add newrelic php-agent  
RUN curl -s https://download.newrelic.com/548C16BF.gpg | apt-key add - \  
&& echo "deb http://apt.newrelic.com/debian/ newrelic non-free" >
/etc/apt/sources.list.d/newrelic.list \  
&& apt-get update \  
&& apt-get install -y newrelic-php5  
COPY confs/newrelic.ini.tpl /usr/local/etc/php/conf.d/newrelic.ini  
  
# Add apache internal vhost for non-public scripts  
COPY confs/apache_vhost_internal.conf /etc/apache2/sites-
available/apache_vhost_internal.conf  
RUN ln -s /etc/apache2/sites-available/apache_vhost_internal.conf
/etc/apache2/sites-enabled/apache_vhost_internal.conf \  
&& echo 'Listen 8081' >> /etc/apache2/ports.conf  
  
# Add scripts  
RUN mkdir -p /var/www/internal \  
&& curl -s https://raw.githubusercontent.com/rlerdorf/opcache-
status/master/opcache.php > /var/www/internal/opcache.php  
COPY confs/clear_cache.php /var/www/internal/clear_cache.php  
  
WORKDIR /var/www  

