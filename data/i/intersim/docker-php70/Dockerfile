FROM php:7.0  
# Install various dependencies  
RUN apt-get update -yqq  
RUN apt-get install -yqq \  
curl \  
git \  
zlib1g-dev \  
libpcre3-dev \  
libicu-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng-dev \  
libtidy-dev \  
libldap2-dev \  
libmagickwand-dev \  
libssl-dev \  
libcurl4-openssl-dev \  
pkg-config  
  
# Install PHP extensions  
RUN docker-php-ext-install zip opcache  
RUN docker-php-ext-install -j$(nproc) mcrypt  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install -j$(nproc) gd  
RUN docker-php-ext-install -j$(nproc) intl  
RUN docker-php-ext-install -j$(nproc) gettext  
RUN docker-php-ext-install -j$(nproc) tidy  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu  
RUN docker-php-ext-install -j$(nproc) ldap  
RUN docker-php-ext-install -j$(nproc) calendar  
RUN docker-php-ext-install -j$(nproc) curl  
  
RUN pecl install imagick  
RUN docker-php-ext-enable imagick  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Install node.js  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash  
RUN apt-get install -y nodejs  
  
# Install gulp  
RUN npm install -g gulp-cli  

