FROM php:5.6.27-cli  
  
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
libxslt1.1 \  
\--no-install-recommends && rm -r /var/lib/apt/lists/*  
  
RUN set -xe \  
&& buildDeps=" \  
zlib1g-dev \  
libicu-dev \  
libpq-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libxslt1-dev \  
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
&& docker-php-ext-install -j$(nproc) mbstring \  
&& docker-php-ext-install -j$(nproc) pcntl \  
&& docker-php-ext-install -j$(nproc) xsl \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& apt-get purge -y --auto-remove -o
APT::AutoRemove::RecommendsImportant=false -o
APT::AutoRemove::SuggestsImportant=false $buildDeps  
  
COPY config/amazon-memcached.ini /usr/local/etc/php/conf.d  
RUN apt-get update && apt-get install -y wget \  
&& wget -O /tmp/AmazonElastiCacheClusterClient.tar.gz https://elasticache-
downloads.s3.amazonaws.com/ClusterClient/PHP-5.6/latest-64bit \  
&& pecl install /tmp/AmazonElastiCacheClusterClient.tar.gz \  
&& rm /tmp/AmazonElastiCacheClusterClient.tar.gz  
  
CMD ["/usr/local/bin/run-perms-php"]  
  

