FROM alpine:edge  
MAINTAINER Marco Foggiato <bitti06@gmail.com>  
  
LABEL caddy_version="0.9.5" architecture="amd64"  
ARG plugins=git,filemanager,realip,multipass  
RUN set -x && \  
echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade  
  
RUN apk add --update --no-cache \  
openssh-client \  
wget \  
git \  
tar \  
curl \  
php7 \  
php7-memcached \  
php7-mysqlnd \  
php7-dom \  
php7-ctype \  
php7-curl \  
php7-fpm \  
php7-gd \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqli \  
php7-opcache \  
php7-pdo \  
php7-pdo_mysql \  
php7-posix \  
php7-session \  
php7-xml \  
php7-iconv \  
php7-phar \  
php7-openssl \  
php7-zip \  
php7-zlib  
  
RUN rm -rf /var/cache/apk/*  
RUN rm -rf /etc/php7/php.ini  
COPY php.ini /etc/php7/php.ini  
  
EXPOSE 80  
# essential php libs  
# allow environment variable access.  
# RUN echo "clear_env = no" >> /etc/php5/php-fpm.conf  
WORKDIR /  
# install caddy (own build)  
#RUN rm -rf /usr/bin/caddy  
#COPY caddy /usr/bin/  
# install caddy (from official site)  
RUN curl --silent --show-error --fail --location \  
\--header "Accept: application/tar+gzip, application/x-gzip,
application/octet-stream" -o - \  
"https://caddyserver.com/download/build?os=linux&arch=amd64&features=${plugins}"
\  
| tar --no-same-owner -C /usr/bin/ -xz caddy \  
&& chmod 0755 /usr/bin/caddy \  
&& /usr/bin/caddy -version  
  
  
COPY start.sh /  
CMD [ "/start.sh" ]  

