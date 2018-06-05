# AIRE's container to execute PHP using php-fpm.  
FROM php:5.6.26-fpm-alpine  
MAINTAINER kristen.gilden@i-smith.ee  
  
# These dependencies and commands should be necessary to run AIRE in
production.  
# We are currently using a single Dockerfile for the sake of simplicity.  
# Installs & enables necessary PHP extensions.  
RUN set -xe \  
&& apk add --no-cache --virtual .build-deps \  
# for intl  
zlib-dev \  
icu-dev \  
icu \  
# for soap  
libxml2-dev \  
# for imagick  
imagemagick-dev \  
autoconf \  
g++ \  
make \  
libtool \  
&& NPROC=$(grep -c ^processor /proc/cpuinfo 2>/dev/null || 1) \  
&& docker-php-ext-install -j$NPROC \  
intl \  
soap \  
pdo_mysql \  
pcntl \  
zip \  
shmop \  
&& pecl install imagick && docker-php-ext-enable imagick \  
&& pecl install apcu-4.0.11 \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add \--no-cache --virtual .php-rundeps $runDeps \  
&& apk del .build-deps  
  
# Installs wkhtmltopdf to generate PDFs from web pages using WebKit.  
RUN apk add --no-cache libxrender \  
&& curl -sS -L
https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.4/wkhtmltox-0.12.4_linux-
generic-amd64.tar.xz | tar -Jxf - \  
&& mv wkhtmltox/bin/wkhtmltopdf /usr/local/bin/wkhtmltopdf \  
&& rm -rf wkhtmltox  
  
COPY php.ini /usr/local/etc/php/  
WORKDIR /usr/share/nginx/html/  
  
# These dependencies and commands are required additionally for testing and  
# building AIRE.  
# For updating, grab a SHA from
https://github.com/composer/getcomposer.org/commits/master.  
# If this is not working, please refer to
https://getcomposer.org/doc/faqs/how-to-install-composer-programmatically.md.  
RUN curl -sS
https://raw.githubusercontent.com/composer/getcomposer.org/1b137f8bf6db3e79a38a5bc45324414a6b1f9df2/web/installer
| php \  
&& mv composer.phar /usr/local/bin/composer  
  
# Installs NodeJS for asset pipeline  
RUN apk add --no-cache nodejs git \  
&& npm install -g \  
bower@1.7.9 \  
grunt-cli@v1.2.0  
  
# Allows us to use the same UID and GID as the host user. The solution is  
# described at https://denibertovic.com/posts/handling-permissions-with-
docker-volumes/.  
RUN apk add \  
\--no-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/edge/testing \  
gosu  
  
VOLUME ["/config"]  
  
CMD ["php-fpm"]  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
ENTRYPOINT ["/usr/local/bin/entrypoint.sh"]  

