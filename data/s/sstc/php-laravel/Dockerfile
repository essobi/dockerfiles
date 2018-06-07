FROM php:7.0-fpm-alpine  
  
# https://laravel.com/docs/5.4/installation  
###  
# Server Requirements  
###  
# Install openssl  
RUN apk add --no-cache \  
openssl  
  
# Install pdo_mysql  
RUN docker-php-ext-install pdo_mysql  
  
# Install mbstring  
RUN docker-php-ext-install mbstring  
  
# Install tokenizer  
RUN docker-php-ext-install tokenizer  
  
# Install xml  
RUN apk add --no-cache \  
libxml2 \  
libxml2-dev \  
&& docker-php-ext-install xml \  
&& apk del --no-cache \  
libxml2-dev  
  
# Install composer  
# https://hub.docker.com/r/composer/composer/~/dockerfile/  
# https://getcomposer.org/doc/00-intro.md  
RUN curl -o /tmp/composer-setup.php https://getcomposer.org/installer \  
&& curl -o /tmp/composer-setup.sig https://composer.github.io/installer.sig \  
&& php -r "if (hash('SHA384', file_get_contents('/tmp/composer-setup.php'))
!== trim(file_get_contents('/tmp/composer-setup.sig'))) { echo 'Invalid
installer' . PHP_EOL; exit(1); }" \  
&& php /tmp/composer-setup.php --install-dir=/bin --filename=composer \  
&& rm /tmp/composer-setup.php  
  
###  
# Others  
###  
  
RUN docker-php-ext-install iconv  
  
# $(getconf _NPROCESSORS_ONLN)  
# https://github.com/docker-library/php/issues/225#issuecomment-234773143  
# Install mcrypt  
RUN apk add --no-cache \  
libmcrypt \  
libmcrypt-dev \  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) mcrypt \  
&& apk del --no-cache \  
libmcrypt-dev  
  
# Install gd  
# https://github.com/docker-library/php/issues/225#issuecomment-226870896  
RUN apk add --no-cache \  
freetype \  
libpng \  
libjpeg-turbo \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev \  
&& docker-php-ext-configure gd \  
\--with-gd \  
\--with-freetype-dir=/usr/include/ \  
\--with-png-dir=/usr/include/ \  
\--with-jpeg-dir=/usr/include/ \  
&& docker-php-ext-install -j$(getconf _NPROCESSORS_ONLN) gd \  
&& apk del --no-cache \  
freetype-dev \  
libpng-dev \  
libjpeg-turbo-dev  

