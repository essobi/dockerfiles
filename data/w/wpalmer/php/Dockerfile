FROM php:7.0-apache  
ENV PHP_VERSION 7.0  
RUN set -xe \  
&& buildDeps=" \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libcurl4-openssl-dev \  
libpng-dev \  
libicu-dev \  
libmcrypt-dev \  
libxml2-dev \  
libxslt-dev \  
" \  
&& runDeps=" \  
msmtp \  
" \  
&& phpExt=" \  
bcmath \  
curl \  
gd \  
intl \  
mbstring \  
pdo \  
pdo_mysql \  
simplexml \  
soap \  
xml \  
xsl \  
zip \  
" \  
&& if [ `printf '%s\n%s\n' "$PHP_VERSION" "7.2" | sort -V | sed '1q'` != "7.2"
]; then phpExt="$phpExt mcrypt"; fi \  
&& apt-get update && apt-get install -y $buildDeps $runDeps --no-install-
recommends && rm -rf /var/lib/apt/lists/* \  
&& mkdir -p /usr/include/freetype2/freetype \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install $phpExt \  
&& apt-get purge -y $buildDeps \  
&& cd /usr/bin \  
&& php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" \  
&& php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" \  
&& php composer-setup.php \  
&& php -r "unlink('composer-setup.php');" \  
&& chmod a+x /usr/bin/composer.phar  

