FROM alpine:3.6  
  
RUN apk --update add \  
php7 \  
php7-bcmath \  
php7-dom \  
php7-ctype \  
php7-curl \  
php7-fileinfo \  
php7-fpm \  
php7-gd \  
php7-iconv \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqli \  
php7-opcache \  
php7-openssl \  
php7-redis \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_pgsql \  
php7-pdo_sqlite \  
php7-phar \  
php7-posix \  
php7-session \  
php7-soap \  
php7-xml \  
php7-zlib \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zip \  
php7-dev \  
php7-pear \  
openssl \  
ca-certificates \  
git \  
wget \  
nodejs \  
nodejs-npm  
  
WORKDIR /tmp  
  
RUN wget https://getcomposer.org/installer && php installer && mv
composer.phar /usr/local/bin/composer && chmod +x /usr/local/bin/composer  
RUN npm install -g bower webpack gulp-cli grunt-cli  
  
EXPOSE 9000  
RUN mkdir /run/php && mkdir -p /var/www/html && rm -rf /tmp/*  
  
RUN sed -i 's/\;daemonize = yes/daemonize = no/' /etc/php7/php-fpm.conf  
RUN composer global require "fxp/composer-asset-plugin:^1.3.1"  
  
WORKDIR /var/www/html  
  
  
COPY ./www.conf /etc/php7/php-fpm.d/  
CMD ["php-fpm7","--allow-to-run-as-root"]

