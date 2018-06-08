FROM php:7-fpm  
RUN apt-get update && apt-get install -y libmcrypt-dev wget python  
  
WORKDIR /tmp  
  
ENV LIBRDKAFKA_VERSION=0.9.2  
# etiher download from github or PECL rdkafka-beta (latest)  
# ENV PHPRDKAFKA_VERSION=0.9.1-php7  
RUN wget
https://github.com/edenhill/librdkafka/archive/v${LIBRDKAFKA_VERSION}.tar.gz
&& \  
tar -xvf v${LIBRDKAFKA_VERSION}.tar.gz && \  
cd librdkafka-${LIBRDKAFKA_VERSION} && \  
./configure && make && make install && ldconfig && cd /tmp && \  
rm -rf librdkafka-${LIBRDKAFKA_VERSION} v${LIBRDKAFKA_VERSION}.tar.gz  
  
# RUN wget https://github.com/arnaud-lb/php-
rdkafka/archive/${PHPRDKAFKA_VERSION}.tar.gz && \  
# tar -xvf ${PHPRDKAFKA_VERSION}.tar.gz && \  
# cd php-rdkafka-${PHPRDKAFKA_VERSION} && \  
# phpize && ./configure && make && cd /tmp && \  
# rm -rf ${PHPRDKAFKA_VERSION}.tar.gz php-rdkafka-${PHPRDKAFKA_VERSION}  
RUN docker-php-ext-install mcrypt mbstring tokenizer mysqli pdo_mysql && \  
pecl install -o redis && \  
pecl install channel://pecl.php.net/rdkafka-beta && \  
rm -rf /tmp/pear && \  
echo "extension=redis.so" > /usr/local/etc/php/conf.d/redis.ini && \  
echo "extension=rdkafka.so" > /usr/local/etc/php/conf.d/rdkafka.ini  

