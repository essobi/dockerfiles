FROM alpine:3.6  
MAINTAINER Tommy Muehle <tommy.muehle@gmail.com>  
  
ARG VERSION=0.8.1  
RUN apk --update --progress --no-cache --repository http://dl-
cdn.alpinelinux.org/alpine/v3.6/community add \  
php7 \  
php7-xdebug \  
php7-openssl \  
php7-ctype \  
php7-json \  
php7-phar \  
php7-zlib \  
php7-mbstring \  
php7-tokenizer \  
php7-dom \  
php7-xml \  
php7-xmlwriter  
  
ADD
https://github.com/infection/infection/releases/download/${VERSION}/infection.phar
/usr/local/bin/infection  
ADD
https://github.com/infection/infection/releases/download/${VERSION}/infection.phar.pubkey
/usr/local/bin/infection.pubkey  
  
RUN echo "zend_extension=xdebug.so" > /etc/php7/conf.d/xdebug.ini \  
&& chmod +x /usr/local/bin/infection \  
&& rm -rf /var/cache/apk/* /var/tmp/* /tmp/*  
  
VOLUME /app  
WORKDIR /app  
  
ENTRYPOINT ["infection"]  

