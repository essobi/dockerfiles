FROM vendelev/supervisor  
  
LABEL maintainer="Vendelev Artiom"  
LABEL version="1.0"  
LABEL image="vendelev/php"  
LABEL tag="7.1"  
LABEL description="Image for php-application"  
  
# Install php 7.1 and pinba  
RUN apk add --no-cache \  
nginx \  
git \  
g++ \  
gcc \  
make \  
re2c \  
php7 \  
php7-fpm \  
php7-mbstring \  
php7-iconv \  
php7-mysqli \  
php7-pdo_mysql \  
php7-gd \  
php7-json \  
php7-memcached \  
php7-mcrypt \  
php7-amqp \  
php7-xdebug \  
php7-zip \  
php7-xml \  
php7-simplexml \  
php7-bcmath \  
php7-curl \  
php7-phar \  
php7-zlib \  
php7-pear \  
php7-soap \  
php7-pcntl \  
php7-ctype \  
php7-posix \  
php7-fileinfo \  
php7-session \  
php7-imagick \  
php7-opcache \  
php7-dev \  
php7-openssl \  
php7-redis \  
php7-pgsql\  
php7-intl \  
php7-gmp \  
php7-dom \  
php7-tokenizer \  
php7-xmlwriter \  
&& ln -s /etc/php7 /etc/php \  
&& ln -s /usr/sbin/php-fpm7 /usr/bin/php-fpm \  
&& ln -s /usr/lib/php7 /usr/lib/php \  
&& sed -i 's/127.0.0.1:9000/9000/g' /etc/php/php-fpm.d/www.conf \  
&& sed -i 's/user = nobody/user = nginx/g' /etc/php/php-fpm.d/www.conf \  
&& sed -i 's/group = nobody/group = nginx/g' /etc/php/php-fpm.d/www.conf \  
&& echo "date.timezone = ${TIMEZONE}" >> /etc/php7/php.ini \  
&& sed -i 's/expose_php = .*/expose_php = Off/g' /etc/php7/php.ini \  
&& sed -i 's/post_max_size = .*/post_max_size = 200M/g' /etc/php7/php.ini \  
&& sed -i 's/upload_max_filesize = .*/upload_max_filesize = 50M/g'
/etc/php7/php.ini \  
# Install pinba  
&& git clone https://github.com/tony2001/pinba_extension /tmp/pinba_extension
\  
&& cd /tmp/pinba_extension \  
&& phpize \  
&& ./configure --enable-pinba \  
&& make install \  
# Clean  
&& apk del \  
g++ \  
gcc \  
make \  
re2c \  
autoconf \  
&& rm -frv /var/cache/apk/* \  
&& rm -frv /tmp/pinba_extension  
  
WORKDIR /tmp  
  
# Install composer global bin  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\  
&& php composer-setup.php --install-dir=/bin --filename=composer \  
&& rm -fv composer-setup.php  
  
RUN composer global require --prefer-dist --optimize-autoloader
hirak/prestissimo  
  
RUN mkdir /run/nginx \  
&& mkdir /var/www/logs \  
&& mkdir -p /var/www/web/web \  
&& echo "<?php phpinfo(); ?>" > /var/www/web/web/index.php  
  
ARG GIT_USER_EMAIL=docker@php  
ARG GIT_USER_NAME=Docker-PHP  
  
RUN git config --global user.email ${GIT_USER_EMAIL} \  
&& git config --global user.name ${GIT_USER_NAME}  
  
ADD ./supervisor.d /etc/supervisor.d  
ADD ./pinba.ini /etc/php7/conf.d/20-pinba.ini  
ADD ./xdebug.ini /etc/php7/conf.d/xdebug.ini  
ADD ./default.conf /etc/nginx/conf.d/default.conf  
  
WORKDIR /var/www/web  
  
EXPOSE 80 9000  

