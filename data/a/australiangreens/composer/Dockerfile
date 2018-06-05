FROM composer:1.6  
RUN apk --no-cache add patch freetype-dev libjpeg-turbo-dev libpng-dev &&
docker-php-ext-configure gd \  
\--with-freetype-dir=/usr \  
\--with-png-dir=/usr \  
\--with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
WORKDIR /app  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["composer"]  

