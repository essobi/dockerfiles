FROM php:alpine  
RUN apk add --no-cache coreutils libpng-dev zlib-dev  
RUN docker-php-ext-install -j$(nproc) gd  

