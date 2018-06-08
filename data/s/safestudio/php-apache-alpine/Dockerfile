FROM safestudio/alpine  
  
RUN \  
apk add --update --no-cache \  
apache2 \  
apache2-ctl \  
apache2-error \  
apache2-ssl \  
apache2-utils \  
php7 \  
php7-amqp \  
php7-apache2 \  
php7-bz2 \  
php7-calendar \  
php7-cli \  
php7-ctype \  
php7-curl \  
php7-dom \  
php7-exif \  
php7-fileinfo \  
php7-ftp \  
php7-gettext \  
php7-gmp \  
php7-iconv \  
php7-imagick \  
php7-intl \  
php7-json \  
php7-mbstring \  
php7-mcrypt \  
php7-memcached \  
php7-mysqlnd \  
php7-opcache \  
php7-openssl \  
php7-pcntl \  
php7-pdo \  
php7-pdo_mysql \  
php7-posix \  
php7-phar \  
php7-redis \  
php7-session \  
php7-shmop \  
php7-simplexml \  
php7-sysvmsg \  
php7-sysvsem \  
php7-sysvshm \  
php7-tokenizer \  
php7-wddx \  
php7-xml \  
php7-xmlreader \  
php7-xmlwriter \  
php7-xsl \  
php7-zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN \  
sed -i "s/#LoadModule\ rewrite_module/LoadModule\ rewrite_module/"
/etc/apache2/httpd.conf \  
&& sed -i "s/#LoadModule\ session_module/LoadModule\ session_module/"
/etc/apache2/httpd.conf \  
&& sed -i "s/#LoadModule\ session_cookie_module/LoadModule\
session_cookie_module/" /etc/apache2/httpd.conf \  
&& sed -i "s/#LoadModule\ session_crypto_module/LoadModule\
session_crypto_module/" /etc/apache2/httpd.conf \  
&& sed -ri \  
-e 's!^User\s+\S+!User safestudio!g' \  
-e 's!^Group\s+\S+!Group safestudio!g' \  
-e 's!^#ServerName\s+\S+!ServerName localhost!g' \  
-e 's!^(\s*CustomLog)\s+\S+!\1 /dev/stdout!g' \  
-e 's!^(\s*ErrorLog)\s+\S+!\1 /dev/stderr!g' \  
-e '$aIncludeOptional /safestudio/httpd/*.conf' \  
/etc/apache2/httpd.conf  
  
RUN \  
sed -ri \  
-e 's!^expose_php.*!expose_php = Off!g' \  
-e 's!^variables_order.*!variables_order = "EGPCS"!g' \  
-e 's!^;error_log.*!error_log = /dev/stderr!g' \  
-e 's!^upload_max_filesize.*!upload_max_filesize = 3M!g' \  
-e 's!^;date.timezone.*!date.timezone = Asia/Ho_Chi_Minh!g' \  
-e 's!^session.name.*!session.name = JSESSIONID!g' \  
/etc/php7/php.ini  
  
RUN mkdir -p /run/apache2/  
  
RUN rm -rf /var/cache/apk/*  
  
COPY entrypoint.sh /  
  
EXPOSE 80  
  
CMD ["/entrypoint.sh"]  

