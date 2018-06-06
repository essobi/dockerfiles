FROM php:7.0-fpm  
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
libmcrypt-dev  
  
# Install the PHP mcrypt extention  
RUN docker-php-ext-install mcrypt  
  
# Install the PHP pdo_mysql extention  
RUN docker-php-ext-install pdo_mysql  
  
# Install the PHP gd library  
RUN docker-php-ext-configure gd \  
\--enable-gd-native-ttf \  
\--with-jpeg-dir=/usr/lib \  
\--with-freetype-dir=/usr/include/freetype2 && \  
docker-php-ext-install gd  
  
# Install ZIP  
RUN pecl install zip && docker-php-ext-enable zip  
  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
  
# Update nodejs to stable version  
RUN npm cache clean -f  
RUN npm install -g n  
RUN n stable  
  
# Install Gulp  
RUN npm install -g gulp  
  
# Install PIP  
RUN curl -O https://bootstrap.pypa.io/get-pip.py && python get-pip.py && rm
get-pip.py  
  
# SSH configuration  
RUN mkdir -p ~/.ssh  

