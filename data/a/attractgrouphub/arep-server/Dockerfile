FROM attractgrouphub/alpine-php7-nginx-composer:1.13-nginx-extra  
  
MAINTAINER Amondar  
  
RUN apk --update add supervisor bash git openssl-dev && \  
composer global require "hirak/prestissimo:^0.3"  
  
# Set environment variables to use them in PHP config files  
ENV FPM_PM static  
ENV FPM_PM_MAX_CHILDREN 4  
ENV PHP_DATE_TIMEZONE Europe/Moscow  
ENV PHP_MEMORY_LIMIT 500M  
ENV PHP_POST_MAX_SIZE 200M  
ENV PHP_UPLOAD_MAX_SIZE 200M  
ENV PHP_SMTP localhost  
ENV PHP_SMTP_PORT 25  
ENV PHP_EXTRA_CONFIGURE_ARGS --enable-fpm --with-fpm-user=root --with-fpm-
group=root  
  
  
EXPOSE 80

