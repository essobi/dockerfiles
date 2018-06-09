FROM alpine:3.7  
  
RUN apk --update add \  
php5 \  
php5-common \  
php5-cli \  
php5-fpm \  
php5-opcache \  
php5-xml \  
php5-ctype \  
php5-ftp \  
php5-gd \  
php5-json \  
php5-posix \  
php5-curl \  
php5-dom \  
php5-pdo \  
php5-pdo_mysql \  
php5-sockets \  
php5-zlib \  
php5-mcrypt \  
php5-pcntl \  
php5-mysql \  
php5-mysqli \  
php5-sqlite3 \  
php5-bz2 \  
php5-pear \  
php5-exif \  
php5-phar \  
php5-openssl \  
php5-posix \  
php5-zip \  
php5-calendar \  
php5-iconv \  
php5-imap \  
php5-soap \  
php5-xsl \  
php5-ldap \  
php5-bcmath \  
pcre \  
&& rm -rf /var/cache/apk/*  
  
RUN addgroup www-data -g 82 -S  
RUN adduser www-data -s /bin/sh -G www-data -u 82 -D  
RUN adduser deploy -s /bin/sh -G www-data -u 2500 -D  
RUN ln -s /usr/bin/php5 /usr/bin/php  
  
CMD ["php-fpm5","-F"]  

