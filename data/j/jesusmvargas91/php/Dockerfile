FROM php:7.2-fpm-alpine  
  
# Install modules  
RUN apk add --no-cache postgresql-dev icu-dev \  
&& docker-php-ext-install pdo pdo_pgsql iconv intl opcache mbstring  
  
RUN apk del icu-dev  
  
CMD ["php-fpm"]  

