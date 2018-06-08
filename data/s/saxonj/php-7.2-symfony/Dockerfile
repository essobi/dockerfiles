FROM php:7.2-fpm  
  
RUN cd ~ \  
&& apt-get update \  
&& apt-get install -y \  
wget \  
vim \  
zlib1g-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
libicu-dev \  
libpq-dev \  
libsqlite3-dev \  
libcurl4-openssl-dev \  
libxml2-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \--with-png-dir=/usr/include/ \  
&& docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-configure curl -with-curl=/usr/bin/curl \  
&& docker-php-ext-install -j$(nproc) \  
zip \  
gd \  
bcmath \  
calendar \  
ctype \  
iconv \  
mbstring \  
opcache \  
hash \  
session \  
tokenizer \  
intl \  
pdo \  
pdo_mysql \  
pdo_pgsql \  
pdo_sqlite \  
pgsql \  
mysqli \  
curl \  
soap \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
&& echo 'precedence ::ffff:0:0/96 100' >> /etc/gai.conf  
  
RUN cd ~ \  
&& wget https://phar.phpunit.de/phpunit.phar \  
&& chmod +x phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit  
  
RUN cd ~ \  
&& wget http://curl.haxx.se/ca/cacert.pem \  
&& rm /etc/ssl/certs/ca-certificates.crt \  
&& mv cacert.pem /etc/ssl/certs/ca-certificates.crt \  
&& EXPECTED_SIGNATURE=$(wget -q -O - https://composer.github.io/installer.sig)
\  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& ACTUAL_SIGNATURE=$(php -r "echo hash_file('SHA384', 'composer-
setup.php');") \  
&& if [ "$EXPECTED_SIGNATURE" != "$ACTUAL_SIGNATURE" ]; \  
then \  
>&2 echo 'ERROR: Invalid installer signature'; \  
rm composer-setup.php; \  
exit 1; \  
fi; \  
php composer-setup.php --quiet \  
&& rm composer-setup.php \  
&& mv composer.phar /usr/local/bin/composer  

