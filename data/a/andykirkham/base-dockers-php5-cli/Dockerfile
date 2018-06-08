#FROM debian:jessie  
FROM php:5.6-cli  
MAINTAINER Andy Kirkham <andy@spiders-lair.com>  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ENV DEPS \  
apt-utils \  
ca-certificates \  
file \  
libc-dev \  
pkg-config \  
libffi-dev \  
libssl-dev \  
libxslt1-dev \  
libxml2 \  
libxml2-dev \  
curl \  
libcurl3 \  
libedit2 \  
libsqlite3-0 \  
libxml2 \  
xz-utils \  
vim \  
mlocate \  
wget \  
unzip \  
libmysqlclient-dev \  
libmysqlclient18 \  
mysql-client \  
libbison-dev \  
libcurl4-gnutls-dev \  
libedit-dev \  
libevent-dev \  
libzmq3-dev \  
libnanomsg-dev \  
libmemcached-dev \  
libev-dev \  
librabbitmq-dev \  
librabbitmq1 \  
git  
  
RUN apt-get update && apt-get install -y $DEPS --no-install-recommends  
  
RUN pecl install memcached \  
&& docker-php-ext-enable memcached  
RUN pecl install libevent-0.1.0 \  
&& docker-php-ext-enable libevent  
RUN pecl install zmq-1.1.3 \  
&& docker-php-ext-enable zmq  
  
#RUN docker-php-ext-install -j$(nproc) memcached  
#RUN docker-php-ext-install -j$(nproc) libevent  
#RUN docker-php-ext-install -j$(nproc) amqp  
#RUN docker-php-ext-install -j$(nproc) zeromq  
  
RUN echo $PHP_VER  
  
# Clean up.  
RUN apt-get autoremove -y \  
&& rm -r /var/lib/apt/lists/*  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
  
  

