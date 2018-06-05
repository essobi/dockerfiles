FROM php:7.1-cli  
  
RUN apt-get update && apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libbz2-dev \  
php-pear \  
curl \  
nodejs \  
git \  
wget \  
python \  
python-setuptools \  
npm \  
lftp \  
mosquitto \  
mosquitto-clients \  
&& easy_install pip \  
&& pip install paho-mqtt awscli shyaml \  
&& docker-php-ext-install iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ \--with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install gd \  
&& ln -s /usr/bin/nodejs /usr/bin/node  
  
#Download dependencies  
# Set memory limit  
RUN echo "memory_limit=1024M" > /usr/local/etc/php/conf.d/memory-limit.ini  
  
# Set environmental variables  
ENV COMPOSER_HOME /root/composer  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN wget https://phar.phpunit.de/phpunit.phar && chmod +x phpunit.phar && mv
phpunit.phar /usr/local/bin/phpunit  
  
RUN docker-php-ext-install \  
zip \  
bz2 \  
iconv \  
mcrypt \  
mbstring \  
pdo_mysql  
  
RUN wget -qO- https://deb.nodesource.com/setup_4.x | bash - && apt-get remove
nodejs -y && apt-get install nodejs -y && npm install bower -g && npm install
grunt -g && npm install gulp -g && npm install -g cordova-hot-code-push-cli  
  
CMD ["php"]

