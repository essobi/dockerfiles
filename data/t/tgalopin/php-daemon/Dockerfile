FROM alpine:latest  
  
ENV LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
TERM="xterm"  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/main" >
/etc/apk/repositories && \  
echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk --update add \  
git \  
curl \  
nodejs \  
php7 \  
php7-amqp \  
php7-bcmath \  
php7-curl \  
php7-ctype \  
php7-dom \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-pdo_mysql \  
php7-openssl \  
php7-pcntl \  
php7-pdo \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-phar \  
php7-session \  
php7-xml \  
php7-zip \  
&& rm -rf /var/cache/apk/* \  
&& ln -s /usr/bin/php7 /usr/bin/php \  
&& curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/bin
--filename=composer \  
&& composer global require phpunit/phpunit \  
&& composer global require symfony/symfony \  
&& composer global require symfony/monolog-bundle \  
&& composer global require doctrine/doctrine-bundle \  
&& composer global require sentry/sentry-symfony \  
&& ln -s /root/.composer/vendor/bin/phpunit /usr/local/bin/phpunit \  
&& mkdir /app  
  
COPY php.ini /etc/php7/conf.d/50-setting.ini  
  
WORKDIR /app  

