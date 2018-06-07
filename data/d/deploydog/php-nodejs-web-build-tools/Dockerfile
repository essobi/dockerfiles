FROM php:5.6  
MAINTAINER deploy.dog  
RUN apt-get update -yqq && \  
apt-get install -yqq git zip curl libicu-dev libcurl4-openssl-dev
libfreetype6-dev libgd-dev libmcrypt-dev libjpeg62-turbo-dev libpng12-dev
libbz2-dev php-pear mysql-client libxml2-dev build-essential \  
&& rm -r /var/lib/apt/lists/*  
  
# PHP Extensions  
RUN docker-php-ext-install pdo_mysql  
RUN docker-php-ext-install curl  
RUN docker-php-ext-install intl  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/  
RUN docker-php-ext-install gd  
RUN docker-php-ext-install json  
RUN docker-php-ext-install mbstring  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install xml  
RUN docker-php-ext-install soap  
RUN docker-php-ext-configure bcmath  
RUN docker-php-ext-install bcmath  
RUN docker-php-ext-install bz2  
RUN docker-php-ext-install mcrypt  
  
RUN pecl install apcu-4.0.11  
RUN docker-php-ext-enable apcu  
RUN rm -f /usr/local/etc/php/conf.d/docker-php-ext-apcu.ini  
  
# Copy in APC config  
COPY php/*.ini /usr/local/etc/php/conf.d/  
  
# Memory Limit  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
  
# Time Zone  
RUN echo "date.timezone=Europe/London" > $PHP_INI_DIR/conf.d/date_timezone.ini  
  
# do not use short tags as they cause phpunit.xml.dist to be parsed as PHP  
RUN echo "short_open_tag=Off" > $PHP_INI_DIR/conf.d/short_tags.ini  
  
# Display PHP version  
RUN php --version  
  
# Install Composer and show version  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
RUN composer --version  
  
# Install Node.JS and show version  
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash -  
RUN apt-get install -yqq nodejs  
RUN nodejs --version  
RUN npm --version  
  
# Install Grunt, Gulp, Less, Bower, webpack, Browserify, etc through NPM  
RUN npm install --global grunt-cli  
RUN npm install --global gulp  
RUN npm install --global less  
RUN npm install --global bower  
RUN npm install --global webpack  
RUN npm install --global browserify  
  
# Install Ruby  
RUN apt-get install ruby-full -yqq  
  
# Install SASS  
RUN gem install sass --no-user-install  
RUN sass -v  
  
# Install Yarn  
RUN curl -sS https://dl.yarnpkg.com/debian/pubkey.gpg | apt-key add -  
RUN echo "deb https://dl.yarnpkg.com/debian/ stable main" | tee
/etc/apt/sources.list.d/yarn.list  
RUN apt-get update -y && apt-get install yarn -yqq  

