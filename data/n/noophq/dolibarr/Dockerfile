FROM php:5.6-apache  
  
RUN a2enmod rewrite  
  
# install the PHP extensions we need  
RUN apt-get update && apt-get install -y libpng12-dev libjpeg-dev && rm -rf
/var/lib/apt/lists/* \  
&& docker-php-ext-configure gd --with-png-dir=/usr --with-jpeg-dir=/usr \  
&& docker-php-ext-install gd  
RUN docker-php-ext-install mysqli  
  
VOLUME /var/www/html  
  
ENV DOLIBARR_VERSION 4.0.2  
ENV DOLIBARR_SHA1 4dbb01385399b6b9e4b66e9ee4d6efc6f5374996  
  
# upstream tarballs include ./wordpress/ so this gives us /usr/src/wordpress  
RUN curl -o dolibarr.tar.gz -SL
https://github.com/Dolibarr/dolibarr/archive/${DOLIBARR_VERSION}.tar.gz \  
&& echo "$DOLIBARR_SHA1 *dolibarr.tar.gz" | sha1sum -c - \  
&& tar -xzf dolibarr.tar.gz -C /usr/src/ \  
&& rm dolibarr.tar.gz \  
&& mv /usr/src/dolibarr-${DOLIBARR_VERSION} /usr/src/dolibarr \  
&& chown -R www-data:www-data /usr/src/dolibarr  
  
COPY docker-entrypoint.sh /entrypoint.sh  
  
# grr, ENTRYPOINT resets CMD now  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

