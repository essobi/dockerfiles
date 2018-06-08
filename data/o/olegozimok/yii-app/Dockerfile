FROM php:7.0.3-fpm  
  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=www-data --with-fpm-
group=www-data --enable-opcache  
  
RUN apt-get update && apt-get install -y libmcrypt-dev libpq-dev \  
&& docker-php-ext-install opcache iconv mcrypt pdo_pgsql pdo_mysql mbstring  
  
ENV YII_ENV Production  
  
ENV RABBITMQ_C_VERSION 0.7.1  
ENV PHP_AMQP_VERSION 1.7.0alpha2  
ENV PHPREDIS_VERSION php7  
  
RUN curl -L -o /tmp/rabbitmq.tar.gz
https://github.com/alanxz/rabbitmq-c/releases/download/v$RABBITMQ_C_VERSION/rabbitmq-c-$RABBITMQ_C_VERSION.tar.gz
\  
&& tar xfz /tmp/rabbitmq.tar.gz \  
&& rm -r /tmp/rabbitmq.tar.gz \  
&& cd rabbitmq-c-$RABBITMQ_C_VERSION \  
&& ./configure \  
&& make \  
&& make install  
  
RUN curl -L -o /tmp/php-amqp.tar.gz https://github.com/pdezwart/php-
amqp/archive/v$PHP_AMQP_VERSION.tar.gz \  
&& tar xfz /tmp/php-amqp.tar.gz \  
&& rm -r /tmp/php-amqp.tar.gz \  
&& mv php-amqp-$PHP_AMQP_VERSION /usr/src/php/ext/php-amqp \  
&& docker-php-ext-install php-amqp  
  
RUN curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/$PHPREDIS_VERSION.tar.gz \  
&& tar xfz /tmp/redis.tar.gz \  
&& rm -r /tmp/redis.tar.gz \  
&& mv phpredis-$PHPREDIS_VERSION /usr/src/php/ext/redis \  
&& docker-php-ext-install redis  
  
CMD /bin/bash -c "php /var/www/html/init --env=$YII_ENV --overwrite=y" && php-
fpm

