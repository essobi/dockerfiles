FROM php:5-apache  
  
WORKDIR /src  
  
RUN apt-get update \  
&& apt-get -qqy install wget libldb-dev libldap2-dev \  
&& wget http://www.facilemanager.com/download/facilemanager-
complete-2.3.3.tar.gz \  
&& tar -xvf facilemanager-complete-2.3.3.tar.gz \  
&& mv facileManager/server/* /var/www/html/  
  
RUN ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& docker-php-ext-install mysql mysqli ldap \  
&& a2enmod rewrite dump_io  
  
COPY fmdns/config.inc.php /var/www/html/  
COPY php.ini /usr/local/etc/php/php.ini

