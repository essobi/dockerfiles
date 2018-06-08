FROM php:fpm  
MAINTAINER finkel <sergio.kudrin@gmail.com>  
  
ARG phpext  
  
RUN apt-get update && apt-get install -y \  
libmcrypt-dev \  
libfreetype6-dev \  
libjpeg62-turbo-dev \  
libpng-dev \  
&& pecl install mcrypt-1.0.1 \  
&& docker-php-ext-enable mcrypt \  
&& apt-get install -y libpq-dev \  
&& apt-get install -y zlib1g-dev libicu-dev g++ \  
&& docker-php-ext-configure gd --with-freetype-dir=/usr/include/ --with-jpeg-
dir=/usr/include/ \  
&& docker-php-ext-install -j$(nproc) gd \  
&& docker-php-ext-install exif \  
&& docker-php-ext-install opcache  
  
RUN if [ "$phpext" != "" ]; then \  
for item in $phpext; do \  
docker-php-ext-install $item; \  
done;\  
fi;  
  
RUN curl -sS -o /tmp/icu.tar.gz -L http://download.icu-
project.org/files/icu4c/58.1/icu4c-58_1-src.tgz && tar -zxf /tmp/icu.tar.gz -C
/tmp && cd /tmp/icu/source && ./configure --prefix=/usr/local && make && make
install  
RUN docker-php-ext-configure intl --with-icu-dir=/usr/local && \  
docker-php-ext-install intl  
  
RUN docker-php-ext-configure pgsql -with-pgsql=/usr/local/pgsql \  
&& docker-php-ext-install pgsql pdo_pgsql  
  
COPY conf/ /usr/local/etc/php-fpm.d/  
CMD ["php-fpm"]  

