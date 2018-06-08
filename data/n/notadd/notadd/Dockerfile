FROM php:fpm-alpine  
MAINTAINER HuadongZuo <admin@zuohuadong.cn>  
# RUN apk update && \  
# apk upgrade  
ARG
plugins=http.cgi,http.cors,http.filemanager,http.git,http.proxyprotocol,http.realip,http.upload,net  
  
RUN echo "http://nl.alpinelinux.org/alpine/latest-stable/main" >
/etc/apk/repositories \  
&& echo "http://nl.alpinelinux.org/alpine/edge/testing/" >>
/etc/apk/repositories \  
&& echo "http://nl.alpinelinux.org/alpine/edge/community/" >>
/etc/apk/repositories \  
&& echo "nameserver 119.29.29.29" >> /etc/resolv.conf && apk update && apk
upgrade && \  
# Install modules : GD mcrypt iconv  
apk add \--no-cache openssh-client git tar curl libmcrypt-dev shadow libaio
zlib-dev postgresql-dev libpq freetype-dev autoconf libwebp-dev libjpeg-turbo
libpng-dev libjpeg-turbo-dev && \  
docker-php-ext-configure gd \  
\--with-gd \  
# --with-zlib \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-webp-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ && \  
NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) && \  
docker-php-ext-install -j${NPROC} gd && \  
# apk del --no-cache libpng-dev libjpeg-turbo-dev libwebp-dev  
set -x && \  
apk --no-cache add -t .build-deps \  
build-base \  
linux-headers \  
gcc \  
g++ && \  
# freetype \  
docker-php-ext-install mcrypt zip iconv && \  
# install php pdo_mysql redis  
docker-php-ext-install pdo_mysql mysqli mbstring json opcache fileinfo && \  
# echo "opcache.enable_cli=1" >> /usr/local/etc/php/conf.d/docker-php-ext-
opcache.ini &&\  
  
docker-php-ext-install pdo_pgsql pgsql  
  
  
RUN { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=2'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini  
  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" \  
"https://getcomposer.org/installer" \  
| php -- --install-dir=/usr/bin --filename=composer  
  
# install caddy  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/linux/amd64?plugins=${plugins}" \  
| tar --no-same-owner -C /usr/bin/ -xz caddy && \  
chmod 0755 /usr/bin/caddy && \  
/usr/bin/caddy -version && \  
mkdir -p /var/www && mkdir -p /var/log && \  
echo "log_errors = On" > /usr/local/etc/php/conf.d/log.ini && \  
echo "error_log=/var/www/log" > /usr/local/etc/php/conf.d/log.ini && \  
cd && \  
apk del .build-deps && \  
rm -rf /tmp/*  
# install notadd  
RUN cd /var/www && \  
git clone https://github.com/notadd/notadd.git && \  
cd notadd && \  
composer install && \  
php notadd vendor:publish --force  
  
RUN cd /var/www && \  
chmod -R 777 ./*  
  
EXPOSE 80 443 2015 9000  
WORKDIR /var/www  
  
COPY Caddyfile /etc/Caddyfile  
  
ENTRYPOINT ["/usr/bin/caddy"]  
CMD ["--conf", "/etc/Caddyfile", "--log", "stdout"]  
  

