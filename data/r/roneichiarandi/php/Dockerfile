FROM alpine:edge  
  
ENV TIMEZONE America/Sao_Paulo  
ENV PHP_MEMORY_LIMIT 128M  
ENV XDEBUG_VERSION 2.5.4  
  
RUN echo "@testing http://dl-4.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories  
RUN apk update && \  
apk upgrade && \  
apk add --update tzdata && \  
cp /usr/share/zoneinfo/${TIMEZONE} /etc/localtime && \  
echo "${TIMEZONE}" > /etc/timezone && \  
apk upgrade && \  
apk add --update tzdata && \  
apk add --update \  
make \  
gcc \  
re2c \  
g++ \  
autoconf \  
bash \  
git \  
curl \  
wget \  
php7-mcrypt@testing \  
php7-mbstring@testing \  
php7-soap@testing \  
php7-openssl@testing \  
php7-gmp@testing \  
php7-pdo_odbc@testing \  
php7-json@testing \  
php7-dom@testing \  
php7-pdo@testing \  
php7-zip@testing \  
php7-pdo_mysql@testing \  
php7-sqlite3@testing \  
php7-pdo_pgsql@testing \  
php7-bcmath@testing \  
php7-odbc@testing \  
php7-pdo_mysql@testing \  
php7-pdo_sqlite@testing \  
php7-gettext@testing \  
php7-xmlreader@testing \  
php7-xmlrpc@testing \  
php7-bz2@testing \  
php7-iconv@testing \  
php7-pdo_dblib@testing \  
php7-curl@testing \  
php7-ctype@testing \  
php7-phar@testing \  
php7-zlib@testing \  
php7-dev@testing \  
php7-common@testing \  
php7-tokenizer@testing \  
php7-simplexml@testing  
  
RUN wget http://xdebug.org/files/xdebug-$XDEBUG_VERSION.tgz \  
&& tar -zxvf xdebug-$XDEBUG_VERSION.tgz \  
&& cd xdebug-$XDEBUG_VERSION && phpize \  
&& ./configure --enable-xdebug && make && make install \  
&& rm -rf /xdebug-$XDEBUG_VERSION* \  
&& echo "zend_extension=$(find /usr/lib/php7/modules/ -name xdebug.so)" >
/etc/php7/php.ini \  
&& echo "xdebug.remote_enable=on" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_handler=dbgp" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_connect_back=1" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_autostart=on" >> /etc/php7/php.ini \  
&& echo "xdebug.remote_port=9004" >> /etc/php7/php.ini  
  
RUN mkdir /app && \  
apk del tzdata && \  
rm -rf /var/cache/apk/*  
  
RUN sed -i "s|;date.timezone =.*|date.timezone = ${TIMEZONE}|"
/etc/php7/php.ini && \  
sed -i "s|memory_limit =.*|memory_limit = ${PHP_MEMORY_LIMIT}|"
/etc/php7/php.ini && \  
sed -i "s/;cgi.fix_pathinfo=1/cgi.fix_pathinfo=0/" /etc/php7/php.ini  
  
# Register the COMPOSER_HOME environment variable  
ENV COMPOSER_HOME /composer  
  
# Add global binary directory to PATH and make sure to re-export it  
ENV PATH /composer/vendor/bin:$PATH  
  
# Allow Composer to be run as root  
ENV COMPOSER_ALLOW_SUPERUSER 1  
  
# Setup the Composer installer  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) {
unlink('/tmp/composer-setup.php'); echo 'Invalid installer' . PHP_EOL;
exit(1); }"  
  
WORKDIR /app  
  
VOLUME ["/app"]  
  
CMD ["sh"]  
ENTRYPOINT ["sh", "-c"]  
  
  

