FROM php:5.6  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
git \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd zip \  
&& apt-get clean  
  
RUN curl https://get.docker.com/builds/Linux/x86_64/docker-latest -o
/usr/local/bin/docker \  
&& chmod +x /usr/local/bin/docker \  
&& curl -sS https://getcomposer.org/installer -o /installer.php \  
&& php /installer.php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer global require phpspec/phpspec \  
&& composer global require phpunit/phpunit \  
&& composer global require phpunit/dbunit \  
&& composer global require phing/phing \  
&& composer global require sebastian/phpcpd \  
&& composer global require phploc/phploc \  
&& composer global require phpmd/phpmd \  
&& composer global require squizlabs/php_codesniffer \  
&& cp -rs /root/.composer/vendor/bin /usr/local/bin/  

