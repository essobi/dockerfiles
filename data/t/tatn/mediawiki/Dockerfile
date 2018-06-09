FROM php:5.6-apache  
MAINTAINER Noguchi Tatsuya <noguchi.ta@gmail.com>  
  
RUN apt-get -y update  
RUN apt-get install -y g++ git imagemagick libicu-dev  
  
RUN pecl install intl  
RUN echo extension=intl.so >> /usr/local/etc/php/conf.d/ext-intl.ini  
RUN docker-php-ext-install mysqli  
RUN a2enmod rewrite  
  
ENV VERSION 1.25.1  
ENV SHORT_VERSION 1.25  
ADD
http://releases.wikimedia.org/mediawiki/$SHORT_VERSION/mediawiki-$VERSION.tar.gz
/usr/src/mediawiki.tar.gz  
  
VOLUME /var/www/html  
RUN rm /var/www/html/index.html && mkdir /usr/src/mediawiki && tar zxf
/usr/src/mediawiki.tar.gz -C /usr/src/mediawiki --strip-components=1 && rm
/usr/src/mediawiki.tar.gz  
  
RUN cp -r /etc/apache2/ /usr/local  
VOLUME /etc/apache2  
  
EXPOSE 80 443  
COPY docker-entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  
CMD ["apache2-foreground"]  

