FROM alpine:edge  
  
RUN apk add --update \  
curl \  
apache2 \  
autoconf alpine-sdk \  
php5 php5-dev \  
php5-apache2 \  
php5-pdo php5-pdo_sqlite php5-pdo_mysql php5-pdo_pgsql \  
php5-imagick php5-gd php5-curl php5-dom php5-phar php5-json php5-ctype \  
&& curl -o xdebug-2.4.0.tgz https://xdebug.org/files/xdebug-2.4.0.tgz \  
&& tar -xvf xdebug-2.4.0.tgz \  
&& cd xdebug-2.4.0 \  
&& phpize \  
&& ./configure \  
&& make \  
&& echo "zend_extension = /xdebug-2.4.0/modules/xdebug.so" >>
/etc/php5/php.ini \  
&& cd ../ \  
&& rm xdebug-2.4.0.tgz \  
&& apk add --update nodejs \  
&& npm install -g coffee-script less bower \  
&& apk del curl autoconf alpine-sdk \  
&& rm -rf /var/cache/apk/*  

