FROM php:5.6-fpm  
  
RUN apt-get update \  
# imagick  
&& apt-get -y --no-install-recommends install libmagickwand-dev \  
# gd  
&& apt-get install -y --no-install-recommends libfreetype6-dev libjpeg-dev
libpng12-dev \  
# mcrypt  
&& apt-get install -y --no-install-recommends libmcrypt-dev \  
# amqp  
&& apt-get install -y --no-install-recommends libssl-dev \  
&& ( \  
curl -L -o rabbitmq-c-0.8.0.tar.gz
https://github.com/alanxz/rabbitmq-c/releases/download/v0.8.0/rabbitmq-c-0.8.0.tar.gz
\  
&& tar xzf rabbitmq-c-0.8.0.tar.gz \  
&& rm rabbitmq-c-0.8.0.tar.gz \  
&& cd rabbitmq-c-0.8.0 \  
&& ./configure && make \  
&& make install \  
&& cd .. \  
&& rm -rf rabbitmq-c-0.8.0 \  
) \  
# clean up  
&& apt-get autoclean -y \  
&& rm -rf /var/lib/apt/lists/*  
  
RUN \  
# imagick  
echo "autodetect" | pecl install imagick \  
&& docker-php-ext-enable imagick \  
# gd  
&& docker-php-ext-install gd \  
# mcrypt  
&& docker-php-ext-install mcrypt \  
# amqp  
&& pecl install amqp \  
&& docker-php-ext-enable amqp \  
# redis  
&& pecl install redis \  
&& docker-php-ext-enable redis \  
# mysqli  
&& docker-php-ext-install mysqli \  
# xdebug  
&& pecl install xdebug \  
&& docker-php-ext-enable xdebug \  
# clean up  
&& rm -rf /tmp/pear/  

