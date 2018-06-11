FROM wiltongarcia/php-fpm  
  
MAINTAINER Wilton Garcia <wiltonog@gmail.com>  
  
RUN set -x \  
&& apk add \--no-cache --virtual .phpize-deps $PHPIZE_DEPS imagemagick-dev
libtool imagemagick \  
&& pecl install imagick \  
&& docker-php-ext-enable imagick  
  

