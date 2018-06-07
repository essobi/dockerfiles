FROM dearteno/alpine-base  
MAINTAINER Pichate Ins <cogent@cogentwebworks.com>  
  
ENV TIMEZONE Asia/Bangkok  
ENV PHP_MEMORY_LIMIT 512M  
ENV MAX_UPLOAD 50M  
ENV PHP_MAX_FILE_UPLOAD 200  
ENV PHP_MAX_POST 100M  
  
ENV PHALCON_VERSION=2.0.13  
ENV IGBINARY_VERSION=2.0.0  
ENV SOLR_VERSION=2.4.0  
ENV MONGO_VERSION=1.6.14  
ENV MONGODB_VERSION=1.2.5  
ENV PHPREDIS_VERSION 3.1.2  
# Install packages  
# enable edge repository  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
  
RUN apk-install git curl tzdata libcurl curl-dev libxml2 libxml2-dev php5
php5-fpm php5-pear php5-apcu php5-bcmath php5-bz2 php5-cli php5-ctype
php5-curl php5-dom php5-exif php5-gd php5-gettext php5-iconv php5-intl
php5-json php5-mcrypt php5-memcache php5-mysql php5-mysqli php5-openssl
php5-pcntl php5-pdo_mysql php5-pdo_pgsql php5-pdo_sqlite php5-phar php5-posix
php5-soap php5-xcache php5-xmlreader php5-xmlrpc php5-xsl php5-zip php5-zlib  
RUN apk-install php5-dev g++ autoconf make re2c  
#RUN apk-install-edge php5-redis  
# Configure PHP-FPM  
COPY config/fpm-pool.conf /etc/php5/fpm.d/zzz_custom.conf  
COPY config/php.ini /etc/php5/conf.d/zzz_custom.ini  
RUN mkdir -p /var/log/php-fpm  
RUN touch /var/log/php-fpm/fpm-error.log  
###  
# Compile redis  
RUN set -xe && \  
curl -LO https://pecl.php.net/get/redis-${PHPREDIS_VERSION}.tgz && \  
tar zxf redis-${PHPREDIS_VERSION}.tgz && \  
cd redis-${PHPREDIS_VERSION} && \  
phpize && ./configure && \  
make && make install && \  
echo "extension=redis.so" > /etc/php5/conf.d/redis.ini && \  
cd .. && rm -rf redis-${PHPREDIS_VERSION} redis-${PHPREDIS_VERSION}.tgz  
  
# Compile mongo  
RUN set -xe && \  
curl -LO https://pecl.php.net/get/mongo-${MONGO_VERSION}.tgz && \  
tar zxf mongo-${MONGO_VERSION}.tgz && \  
cd mongo-${MONGO_VERSION} && \  
phpize && ./configure && \  
make && make install && \  
echo "extension=mongo.so" > /etc/php5/conf.d/mongo.ini && \  
cd .. && rm -rf mongo-${MONGO_VERSION} mongo-${MONGO_VERSION}.tgz  
  
# Compile mongo  
RUN set -xe && \  
curl -LO https://pecl.php.net/get/mongo-${MONGO_VERSION}.tgz && \  
tar zxf mongo-${MONGO_VERSION}.tgz && \  
cd mongo-${MONGO_VERSION} && \  
phpize && ./configure && \  
make && make install && \  
echo "extension=mongo.so" > /etc/php5/conf.d/mongo.ini && \  
cd .. && rm -rf mongo-${MONGO_VERSION} mongo-${MONGO_VERSION}.tgz  
  
# Compile mongodb  
RUN set -xe && \  
curl -LO https://pecl.php.net/get/mongodb-${MONGODB_VERSION}.tgz && \  
tar zxf mongodb-${MONGODB_VERSION}.tgz && \  
cd mongodb-${MONGODB_VERSION} && \  
phpize && ./configure && \  
make && make install && \  
echo "extension=mongodb.so" > /etc/php5/conf.d/zz_mongodb.ini && \  
cd .. && rm -rf mongodb-${MONGODB_VERSION} mongodb-${MONGODB_VERSION}.tgz  
  
# Compile solr  
RUN set -xe && \  
curl -LO https://pecl.php.net/get/solr-${SOLR_VERSION}.tgz && \  
tar zxf solr-${SOLR_VERSION}.tgz && \  
cd solr-${SOLR_VERSION} && \  
phpize && ./configure && \  
make && make install && \  
echo "extension=solr.so" > /etc/php5/conf.d/solr.ini && \  
cd .. && rm -rf solr-${SOLR_VERSION} solr-${SOLR_VERSION}.tgz  
  
# Compile igbinary  
RUN set -xe && \  
curl -LO
https://github.com/igbinary/igbinary/archive/${IGBINARY_VERSION}.tar.gz && \  
tar zxf ${IGBINARY_VERSION}.tar.gz && \  
cd igbinary-${IGBINARY_VERSION} && \  
phpize && ./configure && \  
make && make install && \  
echo "extension=igbinary.so" > /etc/php5/conf.d/igbinary.ini && \  
cd .. && rm -rf igbinary-${IGBINARY_VERSION} ${IGBINARY_VERSION}.tar.gz  
  
# Compile Phalcon  
RUN set -xe && \  
curl -LO
https://github.com/phalcon/cphalcon/archive/phalcon-v${PHALCON_VERSION}.tar.gz
&& \  
tar xzf phalcon-v${PHALCON_VERSION}.tar.gz && cd cphalcon-
phalcon-v${PHALCON_VERSION}/build && sh install && \  
echo "extension=phalcon.so" > /etc/php5/conf.d/phalcon.ini && \  
cd ../.. && rm -rf phalcon-v${PHALCON_VERSION}.tar.gz cphalcon-
phalcon-v${PHALCON_VERSION}  
  
# SED php.ini  
RUN sed -i -e "s|;daemonize\s*=.*|daemonize = no|" -e "s|listen\s*=.*|listen =
9000|" /etc/php5/php-fpm.conf  
RUN sed -i "s|;*date.timezone =.*|date.timezone = ${TIMEZONE}|i"
/etc/php5/php.ini && \  
sed -i "s|;*memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|i"
/etc/php5/php.ini && \  
sed -i "s|;*upload_max_filesize =.*|upload_max_filesize = ${MAX_UPLOAD}|i"
/etc/php5/php.ini && \  
sed -i "s|;*max_file_uploads =.*|max_file_uploads = ${PHP_MAX_FILE_UPLOAD}|i"
/etc/php5/php.ini && \  
sed -i "s|;*post_max_size =.*|post_max_size = ${PHP_MAX_POST}|i"
/etc/php5/php.ini && \  
sed -i "s|;*cgi.fix_pathinfo=.*|cgi.fix_pathinfo= 0|i" /etc/php5/php.ini  
  
RUN pear channel-update pear.php.net && \  
pear upgrade-all && \  
pear config-set auto_discover 1 && \  
  
# Install composer global bin  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin/ --filename=composer && \  
# PECL workaround  
sed -i "s/ -n / /" $(which pecl) && \  
# Clean up  
apk del tzdata php5-dev g++ autoconf make re2c && \  
rm -rf /var/cache/apk/* && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
# root filesystem (S6 config files)  
COPY rootfs /  
  
EXPOSE 9000  
# S6 init script  
ENTRYPOINT [ "/init" ]  

