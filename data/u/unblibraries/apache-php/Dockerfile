FROM unblibraries/apache:alpine  
MAINTAINER Jacob Sanford <jsanford_at_unb.ca>  
  
ENV COMPOSER_PATH /usr/local/bin  
ENV PHP_ERROR_LOG /proc/self/fd/2  
RUN apk --update add php5-apache2 curl php5-curl php5-cli php5-json php5-phar
php5-openssl && \  
rm -f /var/cache/apk/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=${COMPOSER_PATH} \--filename=composer  
  
COPY conf/apache2/app.conf /etc/apache2/conf.d/app.conf  
COPY conf/php/php.ini /etc/php5/php.ini  
  
COPY scripts /scripts  
RUN chmod -R 755 /scripts  

