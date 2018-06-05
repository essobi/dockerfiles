FROM php:5.6-cli  
MAINTAINER Sergii Kovalev "enasik@gmail.com"  
ARG DEBIAN_FRONTEND=noninteractive  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get upgrade -y && apt-get install --assume-yes apt-
utils  
RUN apt-get install -y zbar-tools --no-install-recommends libmagickwand-dev
zlib1g-dev && docker-php-ext-install zip  
  
RUN rm -rf /var/lib/apt/lists/* \  
&& pecl install imagick-beta \  
&& echo "extension=imagick.so" > /usr/local/etc/php/conf.d/ext-imagick.ini \  
&& apt-get remove -y libmagickwand-dev \  
&& apt-get install -y libmagickwand-6.q16-2 \  
&& apt-get autoremove -y \  
&& apt-get clean  
  
ENV DEBIAN_FRONTEND teletype  
  
COPY . /usr/src/zbar-lambda  
WORKDIR /usr/src/zbar-lambda  
  
RUN php -r "copy('https://getcomposer.org/installer', '/tmp/composer-
setup.php');" \  
&& php /tmp/composer-setup.php --install-dir=/usr/local/bin
--filename=composer \  
&& rm /tmp/composer-setup.php  
  
RUN COMPOSER_ALLOW_SUPERUSER=1 composer install --no-dev --no-interaction
--optimize-autoloader  
  
ENTRYPOINT php -f ./index.php \  
IMAGE_URL=${IMAGE_URL} \  
FUNCTION_NAME=${FUNCTION_NAME} \  
FUNCTION_QUALIFIER=${FUNCTION_QUALIFIER} \  
FUNCTION_TRACE_ID=${FUNCTION_TRACE_ID} \  
AWS_REGION=${AWS_REGION} \  
AWS_KEY=${AWS_KEY} \  
AWS_SECRET=${AWS_SECRET}  

