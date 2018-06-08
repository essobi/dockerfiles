FROM shito/alpine-php7-cli:edge  
MAINTAINER Sebastian Knoth <sk@bytepark.de>  
  
# Add PHP 7  
RUN apk upgrade -U && \  
apk --update --repository=http://dl-4.alpinelinux.org/alpine/edge/testing add
\  
php7-xml \  
php7-xsl \  
php7-pdo_mysql \  
php7-mcrypt \  
php7-curl \  
php7-json \  
php7-fpm \  
php7-phar \  
php7-openssl \  
php7-mysqli \  
php7-ctype \  
php7-opcache \  
php7-mbstring  
  
COPY /rootfs /  
  
RUN mkdir -p /var/log/php-fpm && \  
touch /var/log/php-fpm/fpm-error.log  
  
# Add group and add new user to group  
RUN addgroup php-fpm && \  
adduser -S php-fpm php-fpm  
  
# Small fixes  
RUN rm -fr /var/cache/apk/*  
  
EXPOSE 9000  
ENTRYPOINT ["/usr/bin/php-fpm", "-F"]

