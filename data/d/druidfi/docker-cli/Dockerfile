FROM php:7.2-cli-alpine  
  
# Change repositories to use edge to get latest Yarn and Nodejs  
#RUN sed -i -e 's/v[[:digit:]]\\.[[:digit:]]/edge/g' /etc/apk/repositories  
RUN echo 'http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories  
  
RUN apk update && apk upgrade && \  
apk add --no-cache --virtual .build-deps \  
g++ git make autoconf yaml-dev zip unzip openssh  
  
RUN docker-php-ext-install pdo_mysql  
  
# Install MongoDB drivers  
RUN pecl install mongodb && docker-php-ext-enable mongodb  
  
RUN apk del .build-deps  
  
# Install Composer  
RUN curl -sS https://getcomposer.org/installer | php -- \  
\--install-dir=/usr/local/bin \  
\--filename=composer  
  
ENV COMPOSER_ALLOW_SUPERUSER=1  
# Install Yarn  
RUN apk add yarn  
  
WORKDIR /app1  

