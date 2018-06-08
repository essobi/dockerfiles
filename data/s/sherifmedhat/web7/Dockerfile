FROM php:7-apache  
  
MAINTAINER SherifMedhat  
  
RUN apt-get update && apt-get install -y \  
nano \  
zlib1g-dev \  
libicu-dev \  
g++ \  
zip unzip \  
git \  
libjpeg-dev \  
libpng-dev \  
libfreetype6-dev \  
jpegoptim \  
optipng \  
libmcrypt-dev \  
libmagickwand-dev  
  
RUN pecl channel-update pecl.php.net \  
&& pecl install redis \  
&& pecl install xdebug \  
&& pecl install imagick  
  
RUN docker-php-ext-install -j$(nproc) zip \  
&& docker-php-ext-install -j$(nproc) mysqli \  
&& docker-php-ext-install -j$(nproc) pdo_mysql \  
&& docker-php-ext-install -j$(nproc) gettext \  
&& docker-php-ext-install gd \  
&& docker-php-ext-enable xdebug \  
&& docker-php-ext-enable redis \  
&& docker-php-ext-enable imagick  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ && \  
docker-php-ext-install gd  
  
# Install Composer and make it available in the PATH  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/bin/ --filename=composer  
  
# Install Blackfire  
RUN version=$(php -r "echo PHP_MAJOR_VERSION.PHP_MINOR_VERSION;") \  
&& curl -A "Docker" -o /tmp/blackfire-probe.tar.gz -D - -L -s
https://blackfire.io/api/v1/releases/probe/php/linux/amd64/$version \  
&& tar zxpf /tmp/blackfire-probe.tar.gz -C /tmp \  
&& mv /tmp/blackfire-*.so $(php -r "echo
ini_get('extension_dir');")/blackfire.so \  
&& printf
"extension=blackfire.so\nblackfire.agent_socket=tcp://blackfire:8707\n" >
$PHP_INI_DIR/conf.d/blackfire.ini  
  
ADD http://get.sensiolabs.org/php-cs-fixer.phar /usr/local/bin/php-cs-fixer  
RUN chmod a+x /usr/local/bin/php-cs-fixer  
  
ADD https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar
/usr/local/bin/phpcs  
RUN chmod a+x /usr/local/bin/phpcs  
  
ADD https://squizlabs.github.io/PHP_CodeSniffer/phpcbf.phar
/usr/local/bin/phpcbf  
RUN chmod a+x /usr/local/bin/phpcbf  
  

