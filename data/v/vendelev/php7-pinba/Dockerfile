FROM alpine  
  
ENV TIMEZONE Europe/Moscow  
ENV PHP_DIR /etc/php7  
  
RUN apk update  
  
# Install php 7  
RUN apk add \  
php7 \  
php7-fpm \  
php7-mbstring \  
php7-iconv \  
php7-mysqli \  
php7-gd \  
php7-json \  
php7-memcached \  
php7-mcrypt \  
php7-amqp \  
php7-xdebug \  
php7-zip \  
php7-xml \  
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
php7-zip \  
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
&& ln -s /usr/lib/php7 /usr/lib/php  
  
# Install timezone and pinba  
RUN apk add tzdata \  
git \  
g++ \  
gcc \  
make \  
re2c \  
&& cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime \  
&& echo "${TIMEZONE}" > /etc/timezone  
  
RUN git clone https://github.com/tony2001/pinba_extension /tmp/pinba_extension
\  
&& cd /tmp/pinba_extension \  
&& phpize \  
&& ./configure --enable-pinba \  
&& make install \  
&& touch $PHP_DIR/conf.d/20-pinba.ini \  
&& echo 'extension=pinba.so; pinba.enabled=1' > $PHP_DIR/conf.d/20-pinba.ini  
  
WORKDIR /tmp  
  
# Install composer global bin  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
\\\  
&& php composer-setup.php --install-dir=/bin --filename=composer  
  
# Install phpunit global bin  
RUN composer require "phpunit/phpunit" \--prefer-source --no-interaction \  
&& composer require "phpunit/php-invoker" \--prefer-source --no-interaction \  
&& ln -s /tmp/vendor/bin/phpunit /usr/local/bin/phpunit  
  
# Enable X-Debug  
RUN sed -i 's/\;z/z/g' /etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.remote_enable=on" >> /etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.remote_autostart=true" >> /etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.remote_handler=dbgp" >> /etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.remote_mode=req" >> /etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.remote_port=10000" >> /etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.remote_log=/var/log/xdebug_remote.log" >>
/etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.idekey=PHPSTORM" >> /etc/php7/conf.d/xdebug.ini \  
&& echo "xdebug.remote_connect_back=Off" >> /etc/php7/conf.d/xdebug.ini \  
&& php -m | grep -i xdebug  
  
EXPOSE 9000  
RUN apk del tzdata \  
git \  
g++ \  
gcc \  
make \  
re2c \  
&& rm -fr /var/cache/apk/* \  
&& rm -fr /tmp/pinba_extension  
  
WORKDIR /var/www/web  
  
CMD ["/usr/sbin/php-fpm7", "--nodaemonize"]  

