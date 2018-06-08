FROM php:5-apache  
MAINTAINER Florian Humer <florian.humer@gmail.com>  
  
env VERSION 1.14.8  
RUN apt-get update -y  
RUN apt-get install -y git  
RUN git clone git://github.com/simplesamlphp/simplesamlphp /var/www/html  
  
WORKDIR /var/www/html  
  
RUN cp -r config-templates/* config/  
RUN cp -r metadata-templates/* metadata/  
RUN mkdir /var/www/html/cert  
  
RUN git clone https://github.com/soudis/simplesamlphp-usermanagment.git  
RUN rsync -av simplesamlphp-usermanagment/ ./  
RUN rm -r simplesamlphp-usermanagment  
  
VOLUME /var/www/html/config  
VOLUME /var/www/html/metadata  
VOLUME /var/www/html/cert  
  
# Install the gmp and mcrypt extensions  
RUN apt-get update -y  
RUN apt-get install -y libgmp-dev re2c libmhash-dev libmcrypt-dev libldap2-dev
file  
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/  
RUN docker-php-ext-configure gmp  
RUN docker-php-ext-install gmp  
RUN docker-php-ext-configure mcrypt  
RUN docker-php-ext-install mcrypt  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu  
RUN docker-php-ext-install ldap  
  
RUN apt-get install -y libz-dev libmemcached-dev && \  
pecl install memcached && \  
docker-php-ext-enable memcached  
  
RUN echo extension=gmp.so > $PHP_INI_DIR/conf.d/gmp.ini  
RUN echo extension=mcrypt.so > $PHP_INI_DIR/conf.d/mcrypt.ini  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN php composer.phar install  
  
EXPOSE 80  

