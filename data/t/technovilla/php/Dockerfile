FROM php:5-fpm-alpine  
  
RUN apk update \  
&& apk add c-client imap-dev libmcrypt libmcrypt-dev \  
&& docker-php-ext-configure mysql \  
&& docker-php-ext-configure pdo \  
&& docker-php-ext-configure pdo_mysql \  
&& docker-php-ext-configure mbstring \  
&& docker-php-ext-configure imap \  
&& docker-php-ext-configure mcrypt \  
&& pecl install mailparse-2.1.6 \  
&& docker-php-ext-install mysql pdo pdo_mysql mbstring imap mcrypt \  
&& docker-php-ext-enable mailparse \  
&& apk del imap-dev libmcrypt-dev  

