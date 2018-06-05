FROM php:7-apache  
  
WORKDIR /composer  
ADD
https://raw.githubusercontent.com/composer/getcomposer.org/master/web/installer
setup  
RUN php setup --install-dir=. --filename=composer \  
&& mv composer /usr/local/bin/composer \  
&& rm -rf /composer \  
&& apt-get update && DEBIAN_FRONTEND=noninteractive apt-get install -y --no-
install-recommends \  
git zlib1g-dev \  
&& docker-php-ext-install zip \  
&& rm -rf /var/lib/apt/lists/*  
  
COPY ./bootstrap.sh /usr/local/bin/bootstrap  
  
ONBUILD ARG FILE_PREFIX=""  
ONBUILD ARG COMPOSER_ARGS="--no-dev"  
ONBUILD COPY . /var/www/html  
ONBUILD WORKDIR /var/www/html  
ONBUILD RUN /usr/local/bin/bootstrap ${FILE_PREFIX} ${COMPOSER_ARGS}  

