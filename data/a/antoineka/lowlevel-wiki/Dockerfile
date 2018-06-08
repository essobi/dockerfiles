FROM php:7-fpm-alpine  
RUN apk add --no-cache \  
freetype-dev \  
libjpeg-turbo-dev \  
libpng-dev \  
python \  
&& docker-php-ext-install -j4 mysqli gd mbstring iconv opcache  
COPY php/docker-wiki-php-entrypoint /usr/local/bin/  
COPY php/php.ini /usr/local/etc/php/  
ENTRYPOINT ["docker-wiki-php-entrypoint"]  
CMD ["php-fpm"]  
RUN apk add --no-cache wget \  
&& mkdir -p /wiki \  
&& cd /wiki \  
&& wget https://releases.wikimedia.org/mediawiki/1.30/mediawiki-1.30.0.tar.gz
\  
&& tar xf mediawiki-1.30.0.tar.gz \  
&& mv mediawiki-1.30.0 w \  
&& rm mediawiki-1.30.0.tar.gz \  
&& apk del wget  
COPY root/ /wiki/  

