FROM php:7.1-apache  
  
RUN apt-get update && \  
apt-get install -y git zip unzip  
# pecl install apcu-5.1.5 && echo "extension=apcu.so" >
/usr/local/etc/php/conf.d/apcu.ini && \  
# pecl install apcu_bc-1.0.3 && echo "extension=apc.so" >
/usr/local/etc/php/conf.d/z_apc.ini && \  
# apt-get -y remove autoconf g++ gcc libc-dev make pkg-config re2c && \  
# apt-get -y autoremove && \  
# apt-get clean && \  
# rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* &&\  
# rm -rf /usr/share/doc /usr/share/man  
COPY ./apache/php.ini /usr/local/etc/php/  
  
COPY ./apache/site.conf /etc/apache2/sites-available/  
  
RUN a2dissite \\* && mkdir -p /srv && \  
a2enmod headers rewrite && a2ensite site.conf  
  
WORKDIR /srv  
  
COPY . /srv  
  
RUN php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');"
&& \  
php composer-setup.php && \  
php -r "unlink('composer-setup.php');" && \  
mv composer.phar / && \  
php /composer.phar install -o  

