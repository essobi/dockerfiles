FROM php:fpm-alpine  
  
ENV PATH="/var/www/vendor/bin:${PATH}"  
USER root  
  
RUN ln -snf /usr/share/zoneinfo/Europe/Rome /etc/localtime && \  
echo Europe/Rome > /etc/timezone && \  
apk add --update \  
curl \  
supervisor \  
coreutils \  
libjpeg-turbo-dev \  
libpng-dev \  
freetype-dev \  
icu-dev \  
libxml2-dev \  
git \  
openldap-dev && \  
docker-php-ext-install gd pdo pdo_mysql mysqli bcmath zip intl ldap soap && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
rm -fr /var/cache/apk/* && \  
rm -fr /usr/local/etc/php-fpm.d/*  
  
COPY ./conf/php.ini /usr/local/etc/php/conf.d/  
COPY ./conf/php-fpm-pool.conf /usr/local/etc/php-fpm.d/  
WORKDIR /var/www  
EXPOSE 9000  
CMD ["php-fpm", "-R"]  

