FROM attractgrouphub/alpine-php7-nginx-composer:1.13-nginx-extra  
  
MAINTAINER Amondar  
  
RUN apk --update add supervisor nodejs bash git openssl-dev g++ autoconf make
curl  
RUN npm install --global gulp && \  
npm install --global yarn && \  
composer global require "hirak/prestissimo:^0.3"  
  
# Install mongo  
RUN pecl install mongodb  
RUN echo "extension=mongodb.so" > /usr/local/etc/php/conf.d/mongodb.ini  
RUN apk del --no-cache autoconf  
  
# Set environment variables to use them in PHP config files  
ENV FPM_PM static  
ENV FPM_PM_MAX_CHILDREN 4  
ENV PHP_DATE_TIMEZONE Europe/Moscow  
ENV PHP_MEMORY_LIMIT 500M  
ENV PHP_POST_MAX_SIZE 512M  
ENV PHP_UPLOAD_MAX_SIZE 512M  
ENV PHP_SMTP localhost  
ENV PHP_SMTP_PORT 25  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=root --with-fpm-
group=root  
  
  
EXPOSE 80

