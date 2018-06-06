FROM comicrelief/php-slim:7.1  
  
RUN apt-get update -y \  
&& apt-get install -y cmake libgmp-dev libpng-dev libssl-dev \  
&& docker-php-ext-install gd \  
&& docker-php-ext-install gmp  
  
# Required for PhpAmqpLib  
RUN docker-php-ext-install bcmath  
  
RUN curl -L -o /tmp/amqp.tar.gz
https://github.com/alanxz/rabbitmq-c/releases/download/v0.8.0/rabbitmq-c-0.8.0.tar.gz
\  
&& tar xfz /tmp/amqp.tar.gz \  
&& rm -r /tmp/amqp.tar.gz \  
&& mkdir -p /usr/src/php/ext \  
&& mv rabbitmq-c-0.8.0 /usr/src/php/ext/amqp \  
&& cd /usr/src/php/ext/amqp \  
&& ./configure \  
&& cmake -ENABLE_SSL_SUPPORT=ON . \  
&& cmake --build . --target install  
  
RUN pecl install amqp-1.9.0 && \  
docker-php-ext-enable amqp && \  
rm -rf /tmp/*  

