FROM php:7.2-fpm  
  
MAINTAINER Jean Traullé  
  
RUN apt-get update && apt install -y \  
# Gestion des polices avec GD  
freetype* \  
libfontconfig1 \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
# Pour cloner avec composer si nécessaire  
git \  
# Pour wkhtmltopdf  
libxrender1 \  
# Pour intl  
libicu57 libicu-dev \  
# Pour l'optimisation des images  
jpegoptim optipng pngquant gifsicle \  
&& docker-php-ext-install -j$(nproc) iconv intl pdo pdo_mysql zip \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& pecl install redis-4.0.0 \  
&& docker-php-ext-enable redis \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& apt-get remove -qqy libfreetype6-dev libjpeg62-turbo-dev libpng-dev libicu-
dev \  
&& apt-get autoremove -qqy \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& rm -rf /tmp/* \  
# set recommended opcache PHP.ini settings  
# see https://secure.php.net/manual/en/opcache.installation.php  
&& { \  
echo 'opcache.memory_consumption=128'; \  
echo 'opcache.interned_strings_buffer=8'; \  
echo 'opcache.max_accelerated_files=4000'; \  
echo 'opcache.revalidate_freq=60'; \  
echo 'opcache.fast_shutdown=1'; \  
echo 'opcache.enable_cli=1'; \  
} > /usr/local/etc/php/conf.d/opcache-recommended.ini \  
&& sed -i -e 's/listen.*/listen = 0.0.0.0:9000/' /usr/local/etc/php-fpm.conf \  
&& echo "expose_php=0" > /usr/local/etc/php/php.ini  
  
CMD ["php-fpm"]  

