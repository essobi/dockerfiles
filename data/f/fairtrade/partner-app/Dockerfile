FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y \  
freetds-dev \  
libicu-dev \  
libpq-dev \  
libmcrypt-dev \  
libxml2-dev \  
git \  
curl \  
&& rm -r /var/lib/apt/lists/* \  
&& cp -s /usr/lib/x86_64-linux-gnu/libsybdb.so /usr/lib/ \  
&& docker-php-ext-configure pdo_mysql --with-pdo-mysql=mysqlnd \  
&& docker-php-ext-install \  
intl \  
mbstring \  
mcrypt \  
pcntl \  
pdo \  
pdo_dblib \  
pdo_mysql \  
zip \  
xml \  
tokenizer \  
opcache  
  
# images  
RUN apt-get update \  
&& apt-get -y install \  
libmagickwand-dev \  
\--no-install-recommends \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick \  
&& rm -r /var/lib/apt/lists/*  
  
COPY php.ini /usr/local/etc/php/  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
RUN curl -sL https://deb.nodesource.com/setup_6.x | bash  
RUN apt-get install -y nodejs  
  
RUN npm install -g bower gulp-cli

