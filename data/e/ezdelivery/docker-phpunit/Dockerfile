FROM phpunit/phpunit:4.6.10  
MAINTAINER Pedro Maia <pedro.maia@ezdelivery.co>  
  
# Install modules  
RUN apt-get update && apt-get install -y \  
libcurl4-openssl-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libmcrypt-dev \  
libpng12-dev \  
zlib1g-dev \  
libpq-dev \  
&& docker-php-ext-install tokenizer iconv mcrypt \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install curl gd zip mbstring pdo pgsql pdo_pgsql sockets  
  
VOLUME [ "/data" ]  
WORKDIR [ "/data" ]  
  
ENTRYPOINT []  
CMD []

