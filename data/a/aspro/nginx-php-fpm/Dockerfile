ARG NGINX_VER=1.13  
ARG PHP_VER=7.2  
FROM nginx:${NGINX_VER}-alpine as nginx  
  
FROM php:${PHP_VER}-fpm-alpine  
  
COPY \--from=nginx /etc/nginx /etc/nginx  
COPY \--from=nginx /usr/sbin/nginx /usr/sbin/nginx  
COPY \--from=nginx /usr/share/nginx /usr/share/nginx  
COPY \--from=nginx /usr/lib/nginx /usr/lib/nginx  
COPY \--from=nginx /var/log/nginx /var/log/nginx  
  
RUN addgroup -S nginx \  
&& adduser -D -S -h /var/cache/nginx -s /sbin/nologin -G nginx nginx \  
  
&& ln -s /usr/lib/nginx/modules /etc/nginx/modules \  
  
# Bring in gettext so we can get `envsubst`, then throw  
# the rest away. To do this, we need to install `gettext`  
# then move `envsubst` out of the way so `gettext` can  
# be deleted completely, then move `envsubst` back.  
&& apk add \--no-cache --virtual .gettext gettext \  
&& mv /usr/bin/envsubst /tmp/ \  
\  
&& runDeps="$( \  
scanelf --needed --nobanner --format '%n#p' /usr/sbin/nginx
/usr/lib/nginx/modules/*.so /tmp/envsubst \  
| tr ',' '\n' \  
| sort -u \  
| awk 'system("[ -e /usr/local/lib/" $1 " ]") == 0 { next } { print "so:" $1
}' \  
)" \  
&& apk add --no-cache --virtual .nginx-rundeps $runDeps \  
&& apk del .gettext \  
&& mv /tmp/envsubst /usr/local/bin/ \  
\  
# forward request and error logs to docker log collector  
&& ln -sf /dev/stdout /var/log/nginx/access.log \  
&& ln -sf /dev/stderr /var/log/nginx/error.log \  
  
# php build-dependencies  
&& apk --update add \--virtual build-dependencies \  
build-base \  
autoconf \  
libtool \  
tzdata \  
zlib-dev \  
  
&& apk add \--no-cache --virtual .persistent-deps \  
# for postgres  
postgresql-dev \  
# for intl extension  
icu-dev \  
  
&& cp /usr/share/zoneinfo/Europe/Moscow /etc/localtime \  
  
&& docker-php-ext-configure intl --enable-intl \  
&& docker-php-ext-configure pcntl --enable-pcntl \  
  
# install php modules  
&& docker-php-ext-install \  
pdo \  
pdo_pgsql \  
pdo_mysql \  
pgsql \  
mysqli \  
json \  
zip \  
opcache \  
intl \  
pcntl \  
  
&& pecl install xdebug redis \  
&& docker-php-ext-enable redis \  
  
# remove build-dependencies  
&& apk del build-dependencies \  
&& rm -rf /var/cache/apk/*  
  
  
ARG S6_OVERLAY_VER=1.20.0.0  
ADD https://github.com/just-
containers/s6-overlay/releases/download/v${S6_OVERLAY_VER}/s6-overlay-
amd64.tar.gz /tmp/  
RUN tar xzf /tmp/s6-overlay-amd64.tar.gz -C / \  
&& rm -rf /tmp/*  
  
ADD rootfs /  
  
RUN find /usr/bin -type f -exec chmod +x {} \; \  
&& mkdir -p /app  
  
WORKDIR /app  
EXPOSE 80 9000  
ENTRYPOINT [ "/init" ]  
  
LABEL description="nginx + php image based on Alpine" \  
maintainer="Vladimir <vladimir.wold@gmail.com>"

