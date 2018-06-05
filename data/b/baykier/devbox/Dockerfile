#########################################################################################################  
## Dockerfile for php-fpm 5.6  
##  
  
FROM php:5.6.32-fpm-alpine3.4  
  
MAINTAINER baykier 1035666345@qq.com  
  
## 更新apk源为阿里源  
## http://mirrors.aliyun.com/  
ENV ALPINE_VERSION v3.4  
RUN set -x \  
&& echo https://mirrors.aliyun.com/alpine/${ALPINE_VERSION}/main >
/etc/apk/repositories \  
&& echo https://mirrors.aliyun.com/alpine/${ALPINE_VERSION}/community >>
/etc/apk/repositories  
  
## 安装 memcached  
ENV MEMCACHED_VERSION 2.2.0  
RUN set -x \  
&& apk add --no-cache --virtual .phpize-deps \  
${PHPIZE_DEPS}\  
&& apk add --no-cache libmemcached-dev \  
zlib-dev \  
cyrus-sasl-dev \  
&& wget -O /tmp/memcached-${MEMCACHED_VERSION}.tgz
http://pecl.php.net/get/memcached-${MEMCACHED_VERSION}.tgz \  
&& pecl install /tmp/memcached-${MEMCACHED_VERSION}.tgz \  
&& docker-php-ext-enable memcached \  
&& rm -fr /tmp/memcached-${MEMCACHED_VERSION}.tgz \  
&& apk del .phpize-deps  
  
## 安装 GD  
RUN set -x \  
&& apk add --no-cache --virtual .phpize-deps \  
${PHPIZE_DEPS}\  
&& apk add --no-cache \  
freetype \  
libpng \  
libjpeg-turbo \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev\  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
  
&& docker-php-ext-install gd \  
&& apk del .phpize-deps  
  
## 安装pdo_mysql  
RUN set -x \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-source delete  
  
## 安装redis  
ENV REDIS_VERSION 2.2.8  
RUN set -x \  
&& apk add --no-cache --virtual .phpize-deps \  
${PHPIZE_DEPS}\  
&& wget -O /tmp/redis-${REDIS_VERSION}.tgz
http://pecl.php.net/get/redis-${REDIS_VERSION}.tgz \  
&& pecl install /tmp/redis-${REDIS_VERSION}.tgz \  
&& docker-php-ext-enable redis \  
&& rm -fr /tmp/redis-${REDIS_VERSION}.tgz \  
&& apk del .phpize-deps  
  
## 安装mongo扩展  
ENV MONGO_VERSION 1.6.16  
RUN set -x \  
&& apk add --no-cache --virtual .phpize-deps \  
${PHPIZE_DEPS}\  
&& apk add --no-cache openssl-dev \  
&& wget -O /tmp/mongo-${MONGO_VERSION}.tgz
http://pecl.php.net/get/mongo-${MONGO_VERSION}.tgz \  
&& pecl install /tmp/mongo-${MONGO_VERSION}.tgz \  
&& docker-php-ext-enable mongo \  
&& rm -fr /tmp/mongo-${MONGO_VERSION}.tgz \  
&& apk del .phpize-deps  
  
## 安装zip扩展  
ENV ZIP_VERSION 1.15.2  
RUN set -x \  
&& apk add --no-cache --virtual .phpize-deps \  
${PHPIZE_DEPS}\  
&& wget -O /tmp/zip-${ZIP_VERSION}.tgz
http://pecl.php.net/get/zip-${ZIP_VERSION}.tgz \  
&& pecl install /tmp/zip-${ZIP_VERSION}.tgz \  
&& docker-php-ext-enable zip \  
&& rm -fr /tmp/zip-${ZIP_VERSION}.tgz \  
&& apk del .phpize-deps  
  
##################################################################  
##  
## 安装gosu 解决权限问题  
  
ENV GOSU_VERSION 1.10  
RUN set -x \  
&& apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& chmod +x /usr/local/bin/gosu \  
# verify that the binary works  
&& gosu nobody true \  
&& apk del .gosu-deps  
  
#################################################################################  
##  
## 配置备份  
  
##工作目录  
ENV WORKSPACE="/project"  
  
COPY ./php.ini $PHP_INI_DIR/  
COPY ./php-fpm.conf /usr/local/etc/php-fpm.conf  
COPY ./php-fpm.d/* /usr/local/etc/php-fpm.d/  
  
RUN set -x \  
&& mkdir -p ${WORKSPACE} /var/log/php \  
&& chmod 644 -R /usr/local/etc  
  
  
VOLUME ["${WORKSPACE}"]  
  
##指定工作目录  
  
WORKDIR ${WORKSPACE}  
  
EXPOSE 9000  
  
ENTRYPOINT gosu root php-fpm  
  
  
  

