FROM php:5.6-cli  
  
  
# pdo_mysql, mbstring required by Magento2 command line - Mircea #  
RUN apt-get update -qq \  
&& apt-get install -y \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
libzip-dev \  
&& docker-php-ext-install -j$(nproc) iconv mcrypt mysql pdo_mysql mbstring zip
\  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd  
  
## Required in order to be able to install auto-Magento2 on the command line -
Mircea ##  
RUN apt-get update && apt-get install -y zlib1g-dev libicu-dev g++  
RUN docker-php-ext-configure intl  
RUN docker-php-ext-install intl  
RUN echo "memory_limit=-1" > $PHP_INI_DIR/conf.d/memory-limit.ini  
RUN echo "xdebug.max_nesting_level=200" > $PHP_INI_DIR/conf.d/nesting-
level.ini  
## Required in order to be able to install auto-Magento2 on the command line -
Mircea ##  
# Install composer  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin \  
&& apt-get install -qy --force-yes \  
git  
  
RUN apt-get -y install php5-mcrypt php5-gd unzip wget && \  
rm -fr /var/cache/*  
  
RUN wget https://github.com/Yelp/dumb-init/releases/download/v1.0.0/dumb-
init_1.0.0_amd64.deb  
RUN dpkg -i dumb-init_*.deb  
  
# own gui  
RUN mkdir /app  
COPY ./app /app  
  
# where to install shop  
RUN mkdir /www  
  
# copy git auth (otherwise api rate limit during some installations!)  
COPY ./config/git.auth.json /root/.composer/auth.json  
  
WORKDIR /app  
  
EXPOSE 80  
COPY ./entrypoint.sh /  
ENTRYPOINT ["dumb-init", "/entrypoint.sh"]  

