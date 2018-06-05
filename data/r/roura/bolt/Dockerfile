FROM php:7.2-apache  
  
ENV TERM xterm-256color  
  
ARG NODE_VERSION=8.9.4  
ARG BOLT_VERSION=3.5  
RUN apt-get update && apt-get install -y \  
libpq-dev \  
libpng-dev \  
libjpeg62-turbo-dev \  
libfreetype6-dev \  
libxrender1 \  
libfontconfig1 \  
libicu-dev \  
wget\  
nano  
  
RUN docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd pdo_mysql exif zip \  
&& apt-get clean && rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install intl  
  
RUN a2enmod headers && a2enmod rewrite  
  
COPY ./apache-bolt.conf /etc/apache2/sites-available/000-default.conf  
COPY ./extra-php-config.ini /usr/local/etc/php/conf.d  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer \  
&& composer self-update \  
&& composer global require hirak/prestissimo  
  
RUN wget
https://nodejs.org/download/release/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
-O /opt/node.tar.gz \  
&& cd /opt && tar -zxvf node.tar.gz && rm node.tar.gz && mv
node-v${NODE_VERSION}-linux-x64 node \  
&& ln -s /opt/node/bin/node /usr/local/bin/node && ln -s /opt/node/bin/npm
/usr/local/bin/npm  
  
WORKDIR /var/www  
RUN rm -rf html && composer create-project bolt/composer-
install:^${BOLT_VERSION} html --prefer-dist --no-interaction  
COPY config.yml /var/www/html/app/config/  
  
RUN chown -R www-data:www-data /var/www/html  
  
WORKDIR /var/www/html  

