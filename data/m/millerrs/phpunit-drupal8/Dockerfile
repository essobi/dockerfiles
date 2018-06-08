FROM alpine:3.7  
  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /composer  
ENV PATH /composer/vendor/bin:$PATH  
ENV PHPUNIT_VERSION 4.8  
ENV SIMPLETEST_DB sqlite://tmp/site.sqlite  
  
RUN apk add --no-cache \  
bash \  
curl \  
git \  
php7 \  
php7-curl \  
php7-ctype \  
php7-dom \  
php7-gd \  
php7-iconv \  
php7-json \  
php7-mbstring \  
php7-openssl \  
php7-phar \  
php7-pdo \  
php7-pdo_mysql \  
php7-pdo_sqlite \  
php7-session \  
php7-sqlite3 \  
php7-tokenizer \  
php7-xml \  
php7-zlib \  
&& curl --silent --show-error https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require phpunit/phpunit:~${PHPUNIT_VERSION}
hirak/prestissimo  
  
WORKDIR /app  
  
CMD ["phpunit", "--testsuite=unit,kernel"]

