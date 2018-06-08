FROM php:7.1.5-fpm  
  
#RUN apt-get update  
#RUN apt-get install -y wget  
#RUN apt-get install -y apt-transport-https lsb-release ca-certificates  
#RUN wget -O /etc/apt/trusted.gpg.d/php.gpg
https://packages.sury.org/php/apt.gpg  
#RUN echo "deb https://packages.sury.org/php/ $(lsb_release -sc) main" >
/etc/apt/sources.list.d/php.list  
#RUN apt-get update  
#RUN apt-get remove -y wget  
RUN apt-get update  
RUN apt-get install -y git  
RUN apt-get install -y libmemcached-dev  
RUN apt-get install -y supervisor  
RUN apt-get install -y zlib1g-dev  
RUN apt-get install -y nodejs && ln -s /usr/bin/nodejs /usr/bin/node  
RUN apt-get install -y libicu-dev  
RUN apt-get install -y ghostscript  
RUN apt-get install -y ufraw  
RUN apt-get install -y poppler-utils  
RUN apt-get install -y librsvg2-bin  
RUN apt-get install -y gimp  
RUN apt-get install -y libmagickwand-dev  
RUN apt-get install -y imagemagick  
RUN apt-get install -y p7zip-full  
RUN apt-get install -y libreoffice  
#RUN apt-get install -y php7.1-memcached  
RUN apt-get install -y xvfb  
RUN apt-get install -y wkhtmltopdf  
RUN pecl install imagick-3.4.3  
RUN git clone https://github.com/php-memcached-dev/php-memcached
/usr/src/php/ext/memcached && cd /usr/src/php/ext/memcached && git checkout -b
php7 origin/php7  
RUN docker-php-ext-configure memcached  
RUN docker-php-ext-install zip pdo_mysql intl memcached  
  
RUN curl -sS https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer  
  
RUN ln -sf /dev/stdout /var/log/access.log && ln -sf /dev/stderr
/var/log/error.log  
  
#RUN cp /usr/lib/php/20151012/memcached.so /usr/local/lib/php/extensions/no-
debug-non-zts-20151012/memcached.so  
#RUN cp /usr/lib/php/20151012/igbinary.so /usr/local/lib/php/extensions/no-
debug-non-zts-20151012/igbinary.so  
#RUN cp /usr/lib/php/20151012/msgpack.so /usr/local/lib/php/extensions/no-
debug-non-zts-20151012/msgpack.so  
#RUN cp /usr/lib/php/20160303/memcached.so /usr/local/lib/php/extensions/no-
debug-non-zts-20160303/memcached.so  
#RUN cp /usr/lib/php/20160303/igbinary.so /usr/local/lib/php/extensions/no-
debug-non-zts-20160303/igbinary.so  
#RUN cp /usr/lib/php/20160303/msgpack.so /usr/local/lib/php/extensions/no-
debug-non-zts-20160303/msgpack.so  
#RUN docker-php-ext-install memcached  
#RUN docker-php-ext-enable memcached  
WORKDIR /var/app/current  
CMD ["/bin/bash", "start.sh"]  

