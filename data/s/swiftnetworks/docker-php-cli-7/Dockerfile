FROM php:7.1.10-cli  
  
COPY config/swift.ini /usr/local/etc/php/conf.d  
COPY run-perms-php /usr/local/bin  
  
RUN chmod 755 /usr/local/bin/run-perms-php  
  
RUN usermod -u 1000 -s /bin/bash www-data  
  
RUN apt-get update && apt-get install -y \  
libfreetype6 \  
libpng12-0 \  
libmcrypt4 \  
libgssrpc4 \  
libjpeg62-turbo \  
libicu52 \  
libpq5 \  
libkdb5-7 \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN set -xe \  
&& buildDeps=" \  
zlib1g-dev \  
libicu-dev \  
libpq-dev \  
libxml2-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
" \  
&& apt-get update && apt-get install -y $buildDeps --no-install-recommends \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-enable opcache \  
&& docker-php-ext-install -j$(nproc) zip \  
&& docker-php-ext-install -j$(nproc) intl \  
&& docker-php-ext-install -j$(nproc) pdo_pgsql \  
&& docker-php-ext-install -j$(nproc) iconv \  
&& docker-php-ext-install -j$(nproc) mcrypt \  
&& docker-php-ext-install -j$(nproc) bcmath \  
&& docker-php-ext-install -j$(nproc) soap \  
&& docker-php-ext-install -j$(nproc) intl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
CMD ["/usr/local/bin/run-perms-php"]  
  

