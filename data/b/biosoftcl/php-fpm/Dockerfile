FROM php:7.0  
LABEL maintainer="Eduardo Aros <eduardo.aros@biosoft.cl>" \  
version="1.0"  
  
RUN apt-get update && \  
apt-get install -y \  
git \  
unzip \  
openssh-client \  
libpq-dev \  
libmcrypt-dev \  
&& apt-get clean  
  
RUN docker-php-ext-install bcmath  
  
RUN docker-php-ext-install mcrypt  
  
RUN docker-php-ext-install pdo_pgsql  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer

