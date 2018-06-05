FROM php:7.1.4-cli  
  
MAINTAINER Mathew Peterson <mathewpeterson@me.com>  
  
COPY bin/* /usr/local/bin/  
COPY conf/php.ini /usr/local/etc/php/conf.d/  
  
RUN apt-install \  
apt-utils \  
git \  
less \  
libmemcached-dev \  
libssl-dev \  
vim  
  
RUN curl -sS -o /tmp/icu.tar.gz -L http://download.icu-
project.org/files/icu4c/57.1/icu4c-57_1-src.tgz \  
&& tar -zxf /tmp/icu.tar.gz -C /tmp && cd /tmp/icu/source \  
&& ./configure --prefix=/usr/local \  
&& make && make install  
  
RUN docker-php-ext-install intl pdo pdo_mysql \  
&& docker-php-ext-enable opcache  
RUN docker-php-pecl-install memcached redis zip  
  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer  
  
RUN echo "phar.readonly = off" > /usr/local/etc/php/conf.d/phar.ini  
  
CMD ["php", "-a"]  

