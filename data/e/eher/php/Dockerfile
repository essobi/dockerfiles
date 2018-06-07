FROM php:alpine  
RUN apk --update --no-cache add \  
autoconf \  
build-base \  
curl \  
git \  
subversion \  
freetype-dev \  
libjpeg-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libbz2 \  
bzip2-dev \  
libstdc++ \  
libxslt-dev \  
openldap-dev \  
make \  
unzip \  
wget && \  
docker-php-ext-install bcmath mcrypt zip bz2 mbstring pcntl xsl && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd && \  
docker-php-ext-configure ldap --with-libdir=lib/ && \  
docker-php-ext-install ldap && \  
apk del build-base  
RUN curl -L -o /tmp/redis.tar.gz
https://github.com/phpredis/phpredis/archive/3.1.2.tar.gz && \  
tar vxfz /tmp/redis.tar.gz && \  
mkdir -p /usr/src/php/ext && \  
mv phpredis-3.1.2 /usr/src/php/ext/redis && \  
rm -r /tmp/redis.tar.gz && \  
docker-php-ext-install redis  
RUN echo "@edge http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
apk add -U --no-cache php7-pear@edge  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
VOLUME ["/app"]  
WORKDIR /app  
CMD ["-"]  
ENTRYPOINT ["php"]  

