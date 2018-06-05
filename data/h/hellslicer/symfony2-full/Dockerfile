FROM php:7.0-fpm-alpine  
  
RUN apk add --update alpine-sdk bash acl rsync gcc autoconf \  
&& docker-php-ext-install -j4 opcache json mysqli pdo_mysql zip mbstring intl
\  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& git clone https://github.com/phpredis/phpredis.git && cd phpredis && git
checkout php7 && phpize && ./configure && make && make install && rm -rf
phpredis \  
&& docker-php-ext-enable redis \  
&& apk del alpine-sdk gcc autoconf  
  
# Composer and PHPUnit  
ENV COMPOSER_HOME /root/composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& curl -O https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && mv
phpunit.phar /usr/local/bin/phpunit  
  
# Symfony2 console shortcuts  
RUN echo '#!/bin/bash' > /usr/local/bin/dev && echo 'php /srv/app/console
--env=dev $@' >> /usr/local/bin/dev && chmod +x /usr/local/bin/dev \  
&& echo '#!/bin/bash' > /usr/local/bin/prod && echo 'php /srv/app/console
--env=prod $@' >> /usr/local/bin/prod && chmod +x /usr/local/bin/prod  
  
WORKDIR /srv  

