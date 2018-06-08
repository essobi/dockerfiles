FROM php:7.1-fpm  
  
RUN apt-get update && apt-get install -y wget zlib1g-dev libicu-dev g++
libmcrypt-dev libpq-dev libldb-dev libldap2-dev git libsodium-dev  
RUN ln -s /usr/lib/x86_64-linux-gnu/libldap.so /usr/lib/libldap.so \  
&& ln -s /usr/lib/x86_64-linux-gnu/liblber.so /usr/lib/liblber.so  
RUN docker-php-ext-configure intl \  
&& docker-php-ext-install intl pdo_pgsql ldap zip mbstring mcrypt  
  
ADD conf/30-custom.ini /usr/local/etc/php/conf.d/30-custom.ini  
  
RUN curl --silent --show-error https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/local/bin/composer  
  
RUN curl --silent --show-error -L -o phpunit.phar
https://phar.phpunit.de/phpunit.phar \  
&& mv phpunit.phar /usr/local/bin/phpunit  
  
RUN curl -L http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar -o php-cs-
fixer \  
&& chmod a+x php-cs-fixer \  
&& mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
RUN pecl install xdebug  
RUN docker-php-ext-enable xdebug  
  
RUN wget https://archive.org/download/zeromq_4.1.4/zeromq-4.1.4.tar.gz \  
&& tar -xvzf zeromq-4.1.4.tar.gz \  
&& cd zeromq-4.1.4 \  
&& ./configure \  
&& make \  
&& make install \  
&& ldconfig \  
&& cd .. \  
&& rm -fr zeromq-4.1.4.tar.gz zeromq-4.1.4/  
  
RUN git clone git://github.com/mkoppanen/php-zmq.git \  
&& cd php-zmq \  
&& phpize && ./configure \  
&& make \  
&& make install \  
&& cd .. \  
&& rm -fr php-zmq \  
&& echo "extension=zmq.so" > /usr/local/etc/php/conf.d/docker-php-ext-zmq.ini  

