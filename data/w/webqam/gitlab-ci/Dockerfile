FROM php:7.1-fpm  
MAINTAINER Benoit Dumas "bdumas@webqam.fr"  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
git \  
curl \  
nodejs \  
nodejs-legacy \  
npm \  
openssh-client \  
rsync \  
build-essential \  
libmemcached-dev \  
libz-dev \  
libpq-dev \  
libjpeg-dev \  
libpng12-dev \  
libfreetype6-dev \  
libssl-dev \  
libmcrypt-dev \  
zip \  
mysql-client \  
git-ftp  
  
# Install the PHP mcrypt extention  
RUN docker-php-ext-install mcrypt  
  
# Install the PHP zip extention  
RUN docker-php-ext-install zip  
  
# Install Xdebug  
RUN pecl install xdebug-2.5.5 && docker-php-ext-enable xdebug  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql  
  
# Install the PHP gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
# Install ZIP  
# RUN pecl install zip && docker-php-ext-enable zip  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install PHP Code sniffer  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar  
RUN mv phpcs.phar /usr/local/bin/phpcs  
RUN chmod a+x /usr/local/bin/phpcs  
  
# Install PHP Lint  
RUN curl -OL
https://raw.githubusercontent.com/overtrue/phplint/master/bin/phplint  
RUN mv phplint /usr/local/bin/phplint  
RUN chmod a+x /usr/local/bin/phplint  
  
# Update nodejs to stable version  
RUN npm cache clean -f  
RUN npm install -g n  
RUN n stable  
  
# Install Gulp  
RUN npm install -g gulp  
  
# Install PIP  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm
get-pip.py  
  
# Install the PHP pcntl extention  
RUN docker-php-ext-install pcntl  
  
# SSH configuration  
RUN mkdir -p ~/.ssh  

