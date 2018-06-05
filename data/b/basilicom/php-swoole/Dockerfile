FROM php:7.2-cli  
MAINTAINER info@basilicom.de  
RUN apt-get update  
RUN pecl install redis \  
&& docker-php-ext-enable redis \  
&& apt install -y libssl-dev \  
&& pecl download swoole-2.1.0 \  
&& tar xvzf swoole-2.1.0.tgz \  
&& cd swoole-2.1.0 \  
&& phpize \  
&& ./configure --enable-openssl \  
&& make \  
&& make install \  
&& echo "extension=swoole.so" > /usr/local/etc/php/conf.d/docker-php-ext-
swoole.ini \  
&& cd .. && rm -rf swoole-2.1.0  

