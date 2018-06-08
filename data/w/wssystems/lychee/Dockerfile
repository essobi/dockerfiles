FROM gliderlabs/alpine:latest  
  
ARG LYCHEE_VERSION=3.1.6  
ENV UID=991 GID=991  
RUN BUILD_DEPS=" \  
imagemagick-dev \  
tar \  
libressl \  
ca-certificates \  
build-base \  
autoconf \  
pcre-dev \  
libtool" \  
&& apk -U upgrade && apk add --no-cache \  
${BUILD_DEPS} \  
nginx \  
php7-mbstring \  
php7-fpm \  
php7-exif \  
php7-gd \  
php7-json \  
php7-mysqli \  
php7-zip \  
php7-session \  
php7-pear \  
php7-dev \  
s6 \  
su-exec \  
imagemagick \  
&& pecl install imagick \  
&& echo "extension=imagick.so" > /etc/php7/conf.d/imagick.ini \  
&& sed -i -e "s/max_execution_time = 30/max_execution_time = 500/g" \  
-e "s/post_max_size = 8M/post_max_size = 500M/g" \  
-e "s/upload_max_filesize = 2M/upload_max_filesize = 100M/g" \  
-e "s/memory_limit = 256M/memory_limit = 512M/g" \  
/etc/php7/php.ini \  
&& mkdir /lychee && cd /lychee \  
&& wget -qO-
https://github.com/electerious/Lychee/archive/v${LYCHEE_VERSION}.tar.gz | tar
xz --strip 1 \  
&& apk del ${BUILD_DEPS} php7-pear php7-dev \  
&& rm -rf /var/cache/apk/* /tmp/*  
  
COPY nginx.conf /etc/nginx/nginx.conf  
COPY php-fpm.conf /etc/php7/php-fpm.conf  
COPY s6.d /etc/s6.d  
COPY run.sh /usr/local/bin/run.sh  
  
RUN chmod +x /usr/local/bin/run.sh /etc/s6.d/*/* /etc/s6.d/.s6-svscan/*  
  
VOLUME /lychee/uploads /lychee/data  
  
EXPOSE 8888  
LABEL maintainer="Tom Paulus <tom@whitestar.systems>"  
  
CMD ["run.sh"]  

