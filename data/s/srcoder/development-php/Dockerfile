FROM php:5.6-fpm  
MAINTAINER Jeroen Boersma <jeroen@srcode.nl>  
  
RUN apt-get update --fix-missing && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
msmtp \  
imagemagick \  
libssl-dev \  
libxml2-dev \  
libicu-dev \  
libxslt-dev \  
wget libcurl4-openssl-dev \  
ssh-client git vim \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN docker-php-ext-install mcrypt bcmath mysql mysqli pdo_mysql mbstring ftp
soap zip opcache intl xsl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd  
  
ENV PHPREDIS_VERSION 2.2.8  
RUN docker-php-source extract \  
&& curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis \  
&& docker-php-source delete  
  
# Install xdebug  
RUN pecl install xdebug-2.5.5 \  
&& rm -rf /tmp/pear  
  
# Install blackfire agent  
RUN export VERSION=`php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;"` \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/${VERSION} \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so `php -r "echo
ini_get('extension_dir');"`/blackfire.so  
  
# Enable debug extension  
RUN echo "extension=blackfire.so\nblackfire.agent_socket=\${BLACKFIRE_PORT}" >
$PHP_INI_DIR/conf.d/blackfire.ini \  
&& echo "zend_extension=`ls /usr/local/lib/php/extensions/no-debug-non-
zts-*/xdebug.so`" > /usr/local/etc/php/conf.d/xdebug.ini  
  
# Install Magerun  
RUN wget -nv https://files.magerun.net/n98-magerun.phar -O
/usr/local/bin/n98-magerun \  
&& chmod +x /usr/local/bin/n98-magerun \  
&& ln -s /usr/local/bin/n98-magerun /usr/local/bin/magerun  
  
# Install Magerun2  
RUN wget -nv https://files.magerun.net/n98-magerun2.phar -O
/usr/local/bin/n98-magerun2 \  
&& chmod +x /usr/local/bin/n98-magerun2 \  
&& ln -s /usr/local/bin/n98-magerun2 /usr/local/bin/magerun2  
  
# Install composer  
RUN wget -nv https://getcomposer.org/installer -O /tmp/composer-setup.php \  
&& php /tmp/composer-setup.php --quiet --install-dir=/usr/local/bin
--filename=composer \  
&& rm /tmp/composer-setup.php  
  
# Copy config files  
COPY conf/php-fpm.conf /usr/local/etc/  
COPY conf/php.ini /usr/local/etc/php/  
  
# Enable PHP cli  
RUN chmod ugo+rX -R /usr/local/etc/php  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=app --with-fpm-
group=app  
  
# Add user and group  
RUN groupadd -g 1000 app && \  
useradd -g 1000 -u 1000 -d /data -s /bin/bash app  
  
WORKDIR /data  

