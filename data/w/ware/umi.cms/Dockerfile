FROM php:7.1-fpm-alpine  
  
RUN set -ex \  
  
&& apk add --update \  
  
&& apk add --no-cache --virtual .deps \  
zlib \  
libpng \  
libjpeg-turbo \  
freetype \  
libxslt \  
openssl \  
libxml2 \  
  
&& apk add --no-cache --virtual .build-deps \  
coreutils \  
zlib-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
freetype-dev \  
libxslt-dev \  
openssl-dev \  
libxml2 \  
  
&& docker-php-ext-configure gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
  
&& docker-php-ext-configure xmlreader \  
CFLAGS="-I/usr/src/php" \  
  
&& docker-php-ext-install -j$(nproc) \  
gd \  
zip \  
xsl \  
phar \  
json \  
iconv \  
mysqli \  
mbstring \  
pdo_mysql \  
xmlreader \  
simplexml \  
# Clean  
&& rm -rf /tmp/* \  
&& apk del --purge .build-deps  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  
  
ARG BUILD_DATE  
ARG VCS_REF  
  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.vcs-url="https://github.com/Dockerware/docker-umi.cms.git" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.schema-version="1.0" \  
org.label-schema.vendor="DockerWare" \  
org.label-schema.name="docker-umi.cms" \  
org.label-schema.description="Docker Community Image packaging for UMI.CMS" \  
org.label-schema.url="https://github.com/Dockerware/docker-umi.cms"  

