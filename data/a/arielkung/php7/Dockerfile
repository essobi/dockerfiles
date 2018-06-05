FROM php  
  
RUN curl -sL https://deb.nodesource.com/setup_4.x | bash  
  
RUN apt-get install -yqq git libicu-dev libmcrypt-dev libvpx-dev libjpeg-dev
libpng-dev libxpm-dev zlib1g-dev libfreetype6-dev libbz2-dev libgmp3-dev
libldap2-dev libpq-dev libsqlite3-dev libaspell-dev libsnmp-dev libpcre3-dev
libtidy-dev build-essential nodejs libxml2-dev webp libjpeg62 zlib1g-dev
imagemagick  
  
RUN docker-php-ext-install mcrypt pdo_mysql intl gd zip bz2 opcache soap pcntl  
  
RUN pecl install xdebug && echo
"zend_extension=/usr/local/lib/php/extensions/no-debug-non-
zts-20160303/xdebug.so" > /usr/local/etc/php/conf.d/docker-php-ext-xdebug.ini  
  
RUN curl --silent --show-error https://getcomposer.org/installer | php && mv
composer.phar /usr/local/bin/composer  
  
RUN npm install --global gulp-cli bower yarn  

