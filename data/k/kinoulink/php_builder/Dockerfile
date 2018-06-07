FROM ubuntu:16.10  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
php-cli \  
php-curl \  
php-zip \  
php-pdo \  
php-gd \  
php-xml \  
php-apcu \  
php-mysql \  
php-intl \  
git  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  
RUN apt-get remove -y curl && \  
rm -rf /var/lib/apt/lists/*  
  
WORKDIR /var/www

