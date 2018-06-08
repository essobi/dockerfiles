FROM php:7.1.14-cli  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN apt-get update && apt-get install -y \  
git \  
unzip \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libicu-dev \  
libpcre3-dev \  
libicu52 \  
&& rm -rf /var/lib/apt/lists/*  
RUN docker-php-ext-install intl \  
&& docker-php-ext-install pdo_mysql \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install zip \  
&& docker-php-ext-install exif \  
&& docker-php-ext-install opcache \  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && composer --version  
RUN mkdir -p /usr/local/bin && curl -LsS https://symfony.com/installer -o
/usr/local/bin/symfony && chmod a+x /usr/local/bin/symfony  
  
# Set timezone  
RUN rm /etc/localtime && ln -s /usr/share/zoneinfo/Europe/Paris /etc/localtime
&& "date"  
  
RUN composer global require --dev "behat/behat"  
RUN composer global require --dev "behat/mink-browserkit-driver"  
RUN composer global require --dev "behat/mink-goutte-driver"  
RUN composer global require --dev "behat/mink-extension"  
RUN composer global require --dev "behat/symfony2-extension"  
RUN composer global require --dev "behatch/contexts"  
  
RUN composer global require "squizlabs/php_codesniffer=*"  
RUN composer global require --dev nekih/symfony-coding-standard:3.x-dev  
  
RUN /root/.composer/vendor/bin/phpcs --config-set installed_paths
/root/.composer/vendor/nekih/symfony-coding-standard  

