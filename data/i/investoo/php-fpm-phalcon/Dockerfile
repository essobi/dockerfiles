FROM php:7.1.10-fpm  
  
RUN apt-get update \  
&& apt-get install -y \  
libxml2-dev \  
libcurl4-openssl-dev \  
libssl-dev \  
pkg-config \  
git  
  
RUN pecl install mongodb -y \  
&& touch /usr/local/etc/php/conf.d30-mongodb.ini \  
&& echo "extension=mongodb.so" | tee /usr/local/etc/php/conf.d/30-mongodb.ini  
  
ENV PHALCON_VERSION 3.2.1  
  
RUN cd /tmp \  
&& curl -sSLO
https://codeload.github.com/phalcon/cphalcon/tar.gz/v$PHALCON_VERSION \  
&& tar xvzf v$PHALCON_VERSION \  
&& cd cphalcon-$PHALCON_VERSION/build \  
&& ./install \  
&& echo "extension=phalcon.so" > /usr/local/etc/php/conf.d/phalcon.ini \  
&& apt-get autoremove -y \  
&& apt-get autoclean -y \  
&& apt-get clean -y \  
&& rm -rf \  
/var/lib/apt/lists/* \  
/tmp/* \  
/var/tmp/* \  
/etc/php5 \  
/etc/php/5* \  
/usr/lib/php/20121212 \  
/usr/lib/php/20131226 \  
/var/log \  
/var/cache  
  
RUN docker-php-ext-install\  
zip \  
soap \  
pdo_mysql  

