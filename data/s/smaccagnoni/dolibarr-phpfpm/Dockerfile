FROM php:7.1-fpm-alpine  
  
RUN apk update && apk add libpng-dev libjpeg-turbo-dev openldap-dev libpng
libjpeg-turbo libldap \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd \  
&& docker-php-ext-configure ldap --with-libdir=lib/ \  
&& docker-php-ext-install ldap \  
&& docker-php-ext-install mysqli \  
&& apk del libpng-dev libjpeg-turbo-dev openldap-dev \  
&& rm /var/cache/apk/*  
  
COPY dolibarr.sh /usr/local/bin/dolibarr.sh  
COPY nginx.conf /etc/nginx/conf.d/dolibarr.conf  
ADD htdocs.tar.gz /var/www/html/  
COPY conf.php /var/www/html/conf/conf.php  
RUN chown -hR root:root /var/www/html  
RUN mkdir /documents  
RUN chown www-data:www-data /documents  
  
VOLUME /etc/nginx/conf.d  
VOLUME /var/www/html  
  
ENTRYPOINT ["dolibarr.sh"]  

