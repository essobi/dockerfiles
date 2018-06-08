FROM ubuntu:14.04  
MAINTAINER Ivan Peevski <ivan@personifycare.com>  
  
ENV PATH /root/.composer/vendor/bin:$PATH  
  
RUN apt-get -y update && \  
apt-get install -y software-properties-common language-pack-en-base && \  
LC_ALL=en_US.UTF-8 add-apt-repository ppa:ondrej/php && \  
apt-get -y update && \  
apt-get install -y \  
git \  
curl \  
unzip && \  
apt-get install -y \  
php7.0-cli \  
php7.0-curl \  
php7.0-gd \  
php7.0-gmp \  
php7.0-redis \  
php7.0-xml \  
php7.0-bcmath \  
php7.0-zip \  
php7.0-mbstring \  
php-ast \  
php7.0-json \  
php7.0-imagick \  
php7.0-dom \  
php7.0-phar \  
php7.0-pdo \  
php7.0-pdo-mysql \  
php7.0-tokenizer \  
php7.0-simplexml \  
php7.0-xmlwriter  
# php7.0-pgsql \  
# php-pear \  
# php7.0-sqlite3 \  
# php7.0-soap \  
# php7.0-pcntl \  
# php7.0-xmlreader  
# php7.0-zlib \  
# php7.0-opcache \  
# php7.0-mcrypt \  
# php7.0-openssl \  
WORKDIR /tmp  
  
RUN curl -fsSL https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require phpunit/phpunit ^5.7 --no-progress --no-scripts
--no-interaction  
  
# Enable X-Debug  
RUN apt-get install -y php-xdebug  
  
VOLUME ["/app"]  
WORKDIR /app  
  
ENTRYPOINT ["phpunit"]  
CMD ["--help"]

