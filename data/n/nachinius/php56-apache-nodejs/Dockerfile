FROM php:5.6-apache  
  
MAINTAINER nachinius <ignacio.peixoto@gmail.com>  
  
# disable interactive  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN PHP_INI_DIR="/usr/local/etc/php"  
  
# PHP Extensions  
#RUN docker-php-ext-install mcrypt zip bz2 mbstring \  
# && docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-
jpeg-dir=/usr/include/ \  
# && docker-php-ext-install gd  
# Memory Limit  
#RUN echo "memory_limit=1024M" > $PHP_INI_DIR/conf.d/memory-limit.ini  
# Time Zone  
RUN echo "date.timezone=${PHP_TIMEZONE:-UTC}" >
$PHP_INI_DIR/conf.d/date_timezone.ini  
  
# install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
ENV NODE_VERSION 0.12.7  
ENV NPM_VERSION 2.14.1  
# installing node  
RUN curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/node-v$NODE_VERSION-
linux-x64.tar.gz" \  
&& curl -SLO "https://nodejs.org/dist/v$NODE_VERSION/SHASUMS256.txt.asc" \  
&& tar -xzf "node-v$NODE_VERSION-linux-x64.tar.gz" -C /usr/local \--strip-
components=1 \  
&& rm "node-v$NODE_VERSION-linux-x64.tar.gz" SHASUMS256.txt.asc \  
&& npm install -g npm@"$NPM_VERSION" \  
&& npm cache clear  
  

