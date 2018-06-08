FROM php:7.1-fpm  
  
MAINTAINER artyom.norin@gmail.com  
  
RUN mkdir -p /var/www/html/question.dev  
  
RUN apt-get update \  
&& apt-get install wget -y \  
&& wget http://download.icu-project.org/files/icu4c/57.1/icu4c-57_1-src.tgz \  
&& gunzip -d < icu4c-57_1-src.tgz | tar xvf - \  
&& cd icu/source \  
&& chmod +x runConfigureICU configure install-sh \  
&& ./runConfigureICU Linux\gcc \  
&& make \  
&& make install \  
&& docker-php-ext-install intl  
  
RUN apt-get install libpq-dev -y && docker-php-ext-install pdo_pgsql  
RUN docker-php-ext-install opcache  
  
RUN wget http://xdebug.org/files/xdebug-2.5.0.tgz \  
&& tar -xvzf xdebug-2.5.0.tgz \  
&& cd xdebug-2.5.0 \  
&& phpize \  
&& ./configure \  
&& make \  
&& cp modules/xdebug.so /usr/local/lib/php/extensions/no-debug-non-
zts-20160303 \  
&& cd .. \  
&& rm -rf xdebug-2.5.0 xdebug-2.5.0.tgz  
  
COPY . /var/www/html/question.dev  
  
VOLUME '/var/www/html/question.dev'  
  
WORKDIR '/var/www/html/question.dev'  
  
CMD ["php-fpm"]  

