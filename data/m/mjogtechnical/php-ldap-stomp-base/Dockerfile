FROM php:5.5-apache  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libldap2-dev \  
libssl-dev \  
libsasl2-dev \  
libxml2-dev \  
libzip-dev && \  
docker-php-ext-configure ldap --with-libdir=lib/x86_64-linux-gnu/ && \  
docker-php-ext-install ldap mcrypt pdo pdo_mysql mbstring soap zip  
  
RUN echo "no" > /tmp/no.txt \  
&& pecl install mongo < /tmp/no.txt \  
&& echo "extension=mongo.so" > /usr/local/etc/php/conf.d/mongo.ini  
RUN curl -SL "https://pecl.php.net/get/stomp-1.0.8.tgz" -o stomp.tgz && \  
mkdir -p /usr/src/stomp && \  
tar -xvzf stomp.tgz -C /usr/src/stomp --strip-components=1 && \  
cd /usr/src/stomp && \  
phpize && \  
./configure --with-libdir=lib64 && make && make install && echo
"extension=stomp.so" > /usr/local/etc/php/conf.d/stomp.ini  

