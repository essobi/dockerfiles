FROM php:7.1-fpm-alpine  
  
RUN apk add --no-cache \  
\--repository http://dl-cdn.alpinelinux.org/alpine/v3.5/community \  
\--virtual .typo3-deps \  
ghostscript \  
graphicsmagick \  
poppler-utils \  
unzip  
  
RUN apk add --no-cache --virtual .build-deps \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
libxml2-dev \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install \  
gd \  
mysqli \  
soap \  
zip \  
&& apk del .build-deps  
  
RUN touch /usr/local/etc/php/conf.d/typo3.ini \  
&& echo "max_execution_time = 240;" >> /usr/local/etc/php/conf.d/typo3.ini \  
&& echo "max_input_vars = 1500;" >> /usr/local/etc/php/conf.d/typo3.ini \  
&& echo "post_max_size = 32M;" >> /usr/local/etc/php/conf.d/typo3.ini \  
&& echo "upload_max_filesize = 32M;" >> /usr/local/etc/php/conf.d/typo3.ini  
  
WORKDIR /app  

