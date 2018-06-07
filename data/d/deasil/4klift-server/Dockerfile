FROM php:7.1-fpm  
  
# utils, build  
RUN apt-get update \  
&& apt-get install git autoconf libssl-dev zlib1g-dev libicu-dev g++ make
cmake libuv-dev libgmp-dev uuid-dev -y  
  
# datastax php-driver fox cassandra  
RUN git clone https://github.com/datastax/php-driver.git /usr/src/datastax-
php-driver \  
&& cd /usr/src/datastax-php-driver \  
&& git checkout --detach v1.2.2 \  
&& git submodule update --init \  
&& cd ext \  
&& ./install.sh \  
&& echo "extension=cassandra.so" > /usr/local/etc/php/conf.d/cassandra.ini  
  
## PHP extensions  
RUN docker-php-ext-install zip mbstring intl opcache bcmath \  
&& echo extension=bcmath.so > /usr/local/etc/php/conf.d/docker-php-ext-
bcmath.ini \  
&& pecl install apcu-5.1.5 \  
&& echo extension=apcu.so > /usr/local/etc/php/conf.d/apcu.ini \  
&& pecl install uuid \  
&& echo extension=uuid.so > /usr/local/etc/php/conf.d/uuid.ini  
  
WORKDIR /app  
  
EXPOSE 9000

