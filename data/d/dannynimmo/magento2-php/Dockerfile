FROM php:7.1.15-fpm-jessie  
  
RUN buildDependencies=" \  
libcurl4-openssl-dev \  
libxml2-dev \  
libpng-dev \  
libjpeg62-turbo-dev \  
libfreetype6-dev \  
libicu-dev \  
libmcrypt-dev \  
libxslt1-dev \  
" \  
&& apt-get -y update \  
&& apt-get -y install ${buildDependencies} \  
&& apt-get clean  
  
RUN phpExtensions=" \  
bcmath \  
ctype \  
curl \  
dom \  
gd \  
hash \  
iconv \  
intl \  
json \  
mbstring \  
mcrypt \  
opcache \  
pdo \  
pdo_mysql \  
simplexml \  
soap \  
xsl \  
zip \  
" \  
\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ --with-png-dir=/usr/include/ \  
&& docker-php-ext-install ${phpExtensions}  
  
RUN composerVersion="1.6.3" \  
&& curl --output /usr/local/bin/composer
https://getcomposer.org/download/${composerVersion}/composer.phar \  
&& chmod +x /usr/local/bin/composer  
  
RUN magerunVersion="2.1.2" \  
&& curl --output /usr/local/bin/magerun
https://files.magerun.net/n98-magerun2-${magerunVersion}.phar \  
&& chmod +x /usr/local/bin/magerun  
  
COPY conf/php.ini /usr/local/etc/php/conf.d/zz_php.ini  

