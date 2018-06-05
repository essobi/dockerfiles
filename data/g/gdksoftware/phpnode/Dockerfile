FROM php:7.1-cli  
RUN apt-get update && \  
apt-get install -y git-core wget git zip unzip zlib1g-dev && \  
docker-php-ext-install mysqli && \  
docker-php-ext-install pdo_mysql && \  
docker-php-ext-install zip && \  
curl -sL https://deb.nodesource.com/setup_7.x | bash - && \  
apt-get install -y nodejs && \  
curl -sS https://getcomposer.org/installer | php \-- --install-
dir=/usr/local/bin --filename=composer  

