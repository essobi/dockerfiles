FROM php:5.6-fpm  
  
RUN apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y
libcurl4-openssl-dev libpng-dev locales locales-all libicu-dev  
RUN docker-php-ext-install ctype gd iconv pdo pdo_mysql mysqli intl  
  
RUN rm -rf /var/cache/apk/* && rm -rf /tmp/*  
  
RUN locale-gen en_US.UTF-8  
RUN locale-gen de_DE.UTF-8  
RUN locale-gen zh_CN.UTF-8  
RUN locale-gen pt_PT.UTF-8  
  
ADD zz_app.ini /usr/local/etc/php/conf.d/  
  
ADD app.pool.conf /usr/local/etc/php-fpm.d/  
  
CMD ["php-fpm"]  
  
EXPOSE 9000  
EXPOSE 9001  

