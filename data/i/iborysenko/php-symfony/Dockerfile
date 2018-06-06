FROM php:7.1-fpm  
LABEL maintainer="ivan.binzz.borysenko@gmail.com"  
  
ENV RABBITMQ_VERSION v0.8.0  
ENV PHP_AMQP_VERSION v1.9.3  
ENV PHP_REDIS_VERSION 3.1.4  
ENV PHP_IMAGICK_VERSION 3.4.3  
ENV TIMEZONE "Europe/Kiev"  
ENV BUILD_DEPS git libpq-dev libzip-dev libicu-dev libssl-dev libmagickwand-
dev libmagickcore-dev unzip cmake  
  
RUN echo "deb http://us.archive.ubuntu.com/ubuntu/ precise main universe" >>
/etc/apt/source.list  
  
# git libssl  
RUN apt-get update \  
&& apt-get install -y ${BUILD_DEPS} \--no-install-recommends  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
# Set timezone  
RUN rm /etc/localtime  
RUN ln -s /usr/share/zoneinfo/${TIMEZONE} /etc/localtime  
RUN "date"  
  
# RabbitMq  
RUN git clone \--branch ${RABBITMQ_VERSION}
https://github.com/alanxz/rabbitmq-c.git /tmp/rabbitmq \  
&& cd /tmp/rabbitmq \  
&& mkdir build && cd build \  
&& cmake .. \  
&& cmake --build . --target install \  
&& rm -r /tmp/rabbitmq  
# AMQP  
RUN git clone \--branch ${PHP_AMQP_VERSION} https://github.com/pdezwart/php-
amqp.git /tmp/php-amqp \  
&& cd /tmp/php-amqp \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -r /tmp/php-amqp  
  
# REDIS  
RUN git clone \--branch ${PHP_REDIS_VERSION}
https://github.com/phpredis/phpredis /tmp/phpredis \  
&& cd /tmp/phpredis \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -r /tmp/phpredis  
  
# IMAGIC  
RUN git clone \--branch ${PHP_IMAGICK_VERSION}
https://github.com/mkoppanen/imagick.git /tmp/imagick \  
&& cd /tmp/imagick \  
&& phpize \  
&& ./configure \  
&& make \  
&& make install \  
&& rm -r /tmp/imagick  
  
RUN docker-php-ext-configure bcmath --enable-bcmath  
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql  
  
RUN docker-php-ext-install \  
bcmath \  
pdo \  
pdo_mysql \  
pdo_pgsql pgsql \  
intl \  
mbstring \  
sockets \  
zip  
  
RUN echo "extension=amqp.so" > /usr/local/etc/php/conf.d/amqp.ini  
RUN echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini  
RUN echo "extension=imagick.so" > /usr/local/etc/php/conf.d/imagick.ini  
  
WORKDIR /var/www/symfony  
  
RUN usermod -u 1000 www-data  
  
RUN echo 'alias sf="php bin/console"' >> ~/.bashrc  
  
RUN php -m  
CMD ["php-fpm"]  

