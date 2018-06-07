FROM alpine:3.4  
WORKDIR /app  
ADD . /app  
  
RUN echo '@main http://nl.alpinelinux.org/alpine/edge/main' >>
/etc/apk/repositories \  
&& echo '@community http://nl.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories \  
&& echo '@testing http://nl.alpinelinux.org/alpine/edge/testing' >>
/etc/apk/repositories \  
&& apk update && apk upgrade \  
&& apk add libressl2.4-libcrypto@main libressl2.4-libssl@main curl@main
php7@community php7-openssl@community php7-zlib@community php7-phar@community
php7-json@community php7-curl@community icu-libs php7-intl@community
php7-mbstring@community \  
&& rm -rf /var/cache/apk/*  
  
RUN ln -s /usr/bin/php7 /usr/bin/php  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require "hirak/prestissimo" \  
&& composer install -o  
RUN composer clear-cache  
  
CMD php bin/console.php $CMD  

