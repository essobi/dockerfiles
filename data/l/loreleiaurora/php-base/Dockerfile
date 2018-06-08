FROM alpine:3.6  
MAINTAINER Lorelei Aurora <iam@l5i.me>  
  
ENV WP_CLI_URL https://github.com/wp-cli/wp-cli/releases/download/v1.3.0/wp-
cli-1.3.0.phar  
  
RUN apk add --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/edge/testing/ --repository http://dl-
cdn.alpinelinux.org/alpine/edge/main/ \  
curl \  
libsodium \  
php7 \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-exif \  
php7-fileinfo \  
php7-fpm \  
php7-gd \  
php7-gettext \  
php7-iconv \  
php7-imap \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-mysqli \  
php7-mysqlnd \  
php7-openssl \  
php7-pdo_mysql \  
php7-phar \  
php7-posix \  
php7-redis \  
php7-simplexml \  
php7-libsodium \  
php7-memcached \  
php7-tokenizer \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zip \  
php7-zlib \  
&& echo 'extension=sodium.so' > /etc/php7/conf.d/50_libsodium.ini \  
\  
&& curl -L -o /usr/bin/wp "${WP_CLI_URL}" \  
&& chmod +x /usr/bin/wp  
  
COPY ./fs /  
  
CMD ["php-fpm7"]  

