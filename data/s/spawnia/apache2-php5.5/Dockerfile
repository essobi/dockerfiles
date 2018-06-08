FROM alpine:3.6  
LABEL maintainer="Benedikt Franke <benedikt.franke@zoho.com>"  
LABEL version="0.1.0"  
LABEL description="An alpine based container with apache2 and php as an apache
module"  
  
RUN apk --update add \  
apache2 \  
php5-apache2 \  
php5-ctype \  
php5-json \  
php5-exif \  
php5-gd \  
php5-pdo \  
php5-mysql \  
php5-pdo_mysql \  
php5-xml \  
php5-dom \  
php5-zip \  
curl \  
php5-cli \  
php5-phar \  
php5-openssl \  
php5-zlib  
  
RUN ln -s /usr/bin/php5 /usr/bin/php  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'544e09ee996cdf60ece3804abc52599c22b1f40f4323403c44d44fdfdd586475ca9813a858088ffbc1f233e9b180f061')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --install-dir=/usr/bin --filename=composer && \  
php -r "unlink('composer-setup.php');"  
  
# this is where apache puts its pid file  
RUN mkdir /run/apache2  
  
RUN mkdir /var/www/htdocs  
RUN mkdir /var/www/htdocs/public  
RUN echo "<?php phpinfo() ?>" > /var/www/htdocs/public/index.php  
  
COPY httpd.conf /etc/apache2/httpd.conf  
  
EXPOSE 80  
WORKDIR /var/www/htdocs  
  
CMD ["httpd", "-D", "FOREGROUND"]  

