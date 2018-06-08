FROM php:cli  
ENV DOCKER_VERSION 17.03.0-ce  
RUN apt-get update && apt-get install -y \  
zlib1g-dev \  
libicu-dev \  
g++ \  
git \  
&& docker-php-ext-install -j$(nproc) bcmath pdo pdo_mysql mysqli opcache zip \  
&& docker-php-ext-configure intl \  
&& docker-php-ext-install -j$(nproc) intl \  
&& curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer \  
&& curl -L -o /tmp/docker-$DOCKER_VERSION.tgz
https://download.docker.com/linux/static/stable/x86_64/docker-$DOCKER_VERSION.tgz
\  
&& tar -xz -C /tmp -f /tmp/docker-$DOCKER_VERSION.tgz \  
&& mv /tmp/docker/* /usr/bin  

