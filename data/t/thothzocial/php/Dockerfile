FROM php:5.6-alpine  
  
RUN apk --no-cache add \  
autoconf \  
curl \  
curl-dev \  
openssl \  
openssl-dev \  
libxml2 \  
libxml2-dev \  
libmcrypt \  
libmcrypt-dev \  
git \  
subversion \  
openssh \  
mercurial \  
tini \  
bash \  
imap-dev \  
pcre-dev \  
zlib-dev \  
geoip-dev \  
postgresql-dev \  
make \  
g++ \  
gcc  
  
RUN echo "memory_limit=-1" > "$PHP_INI_DIR/conf.d/memory-limit.ini" \  
&& echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
"$PHP_INI_DIR/conf.d/date_timezone.ini"  
  
RUN docker-php-ext-install zip \  
&& docker-php-ext-install imap \  
&& docker-php-ext-install bcmath \  
&& docker-php-ext-install mcrypt \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-install pdo_pgsql  
  
RUN pecl install redis && docker-php-ext-enable redis  
RUN pecl install geoip-1.1.1 && docker-php-ext-enable geoip  
RUN pecl install mongodb && docker-php-ext-enable mongodb  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin/ --filename=composer && chmod +x /usr/local/bin/composer  
  
WORKDIR /app  
  
CMD ["php", "-a"]  

