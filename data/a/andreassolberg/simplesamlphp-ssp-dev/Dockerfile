FROM php:7.1-apache  
RUN apt-get update && apt-get install -y \  
ca-certificates unzip curl libcurl4-openssl-dev git \  
nodejs nodejs-legacy \  
libldap2-dev \  
libgmp-dev re2c libmhash-dev libmcrypt-dev file \  
&& rm -rf /var/lib/apt/lists/*  
RUN ln -s /usr/include/x86_64-linux-gnu/gmp.h /usr/local/include/  
RUN docker-php-ext-configure gmp  
RUN docker-php-ext-configure mcrypt  
RUN docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/  
RUN docker-php-ext-install ldap curl gmp mcrypt  
RUN a2enmod remoteip  
  
# ---> Apache configuration <\---  
RUN mkdir -p /app  
WORKDIR /app  
  
COPY www /app/www  
  
# ---> SimpleSAMLphp app <\---  
RUN curl -sS https://getcomposer.org/installer | php  
RUN mv composer.phar /usr/local/bin/composer  
COPY composer.json /app/  
RUN composer update  
RUN mkdir -p /var/log/simplesamlphp  
RUN touch /var/log/simplesamlphp/simplesamlphp.log  
RUN chown www-data /var/log/simplesamlphp/simplesamlphp.log  
#RUN ln -s /app/modules/saml2debug
/app/vendor/simplesamlphp/simplesamlphp/modules/saml2debug  
COPY etc/simplesamlphp-metadata
/app/vendor/simplesamlphp/simplesamlphp/metadata/  
COPY etc/simplesamlphp-config /app/vendor/simplesamlphp/simplesamlphp/config/  
  
RUN rm /etc/apache2/sites-enabled/000-default.conf /etc/apache2/conf-
enabled/other-vhosts-access-log.conf  
COPY etc/simplesamlphp.conf /etc/apache2/sites-enabled/simplesamlphp.conf  
COPY etc/php.ini /usr/local/etc/php/conf.d/php.ini  
  
ENV SERVER_ADMIN "replace.this@acme.org"  
ENV HOST "acme.org"  
ENV HTTPS "http"  
ENV HTTPSON "off"  

