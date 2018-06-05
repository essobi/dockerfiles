FROM php:7.1.15-jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV COMPOSER_ALLOW_SUPERUSER 1  
ENV COMPOSER_HOME /tmp  
ENV GIT_COMMITTER_NAME 'Drucker'  
ENV GIT_COMMITTER_EMAIL 'composer@drucker.com'  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libpcre3-dev \  
curl \  
mysql-client \  
git-core \  
openssl \  
mercurial \  
bash  
  
RUN docker-php-ext-install -j$(nproc) mysqli && \  
docker-php-ext-install -j$(nproc) pdo_mysql && \  
docker-php-ext-install iconv mcrypt && \  
docker-php-ext-configure opcache --enable-opcache && \  
docker-php-ext-install -j$(nproc) opcache && \  
docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install -j$(nproc) gd && \  
docker-php-ext-install -j$(nproc) zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
composer --ansi --version --no-interaction  
  
CMD ["composer"]

