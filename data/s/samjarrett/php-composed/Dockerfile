FROM php:7.0-fpm  
  
RUN set -xe && \  
apt-get -qq update && \  
apt-get -qq install \  
git \  
zlib1g-dev \  
\--no-install-recommends && \  
docker-php-ext-install zip > /dev/null && \  
apt-get clean && \  
rm -r /var/lib/apt/lists/* && \  
curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer && \  
true

