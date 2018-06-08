FROM alpine:edge  
MAINTAINER Danil Kuznetsov <kuznetsov.danil.v@gmail.com>  
  
ENV LANG="en_US.UTF-8" \  
LC_ALL="en_US.UTF-8" \  
LANGUAGE="en_US.UTF-8" \  
TERM="xterm"  
  
ENV TIMEZONE="Europe/Kiev"  
  
RUN set -x \  
&& addgroup -g 82 -S www-data \  
&& adduser -u 82 -D -S -G www-data www-data  
  
RUN echo "http://dl-cdn.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk update && \  
apk upgrade && \  
apk add bash curl mariadb-client ca-certificates && \  
apk add --update tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk add --update \  
php7-intl \  
php7-opcache \  
php7-apcu \  
php7-phar \  
php7-mcrypt \  
php7-openssl \  
php7-json \  
php7-zlib \  
php7-dom \  
php7-pdo \  
php7-pdo_mysql \  
php7-mysqli \  
php7-bcmath \  
php7-gd \  
php7-xmlreader \  
php7-xml \  
php7-iconv \  
php7-curl \  
php7-ctype \  
php7-mbstring \  
php7-zip \  
php7-imap \  
php7-ssh2 \  
php7-posix \  
php7-session \  
php7-fpm  
  
# fix php-fpm "Error relocating /usr/bin/php-fpm: __flt_rounds: symbol not
found" bug  
RUN apk add -u musl  
  
RUN rm -rf /var/cache/apk/* && \  
apk del tzdata  
  
ADD templates/php-fpm.conf /etc/php7/  
ADD templates/run.sh /RUN/run.sh  
RUN chmod u+x /RUN/run.sh  
  
EXPOSE 9000  
VOLUME ["/DATA"]  
VOLUME ["/RUN"]  
  
CMD ["/RUN/run.sh"]

