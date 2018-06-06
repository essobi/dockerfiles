FROM cubeteam/alpine-nginx  
  
LABEL description="A Docker image based on Alpine Linux for running nginx and
PHP-FPM"  
LABEL maintainer="n.vasic@cubeteam.com"  
  
RUN apk --update add \  
php7 \  
php7-common \  
php7-cli \  
php7-fpm \  
php7-bcmath \  
php7-curl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-opcache \  
php7-xml \  
php7-simplexml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-zip \  
php7-bz2 \  
php7-iconv \  
php7-ctype \  
php7-gettext \  
php7-redis \  
php7-sqlite3 \  
php7-phar \  
php7-openssl \  
php7-dom \  
php7-tokenizer \  
php7-gd \  
php7-zlib \  
&& rm -rf /var/cache/apk/*  

