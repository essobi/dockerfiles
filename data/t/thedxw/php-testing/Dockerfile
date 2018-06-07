FROM php:7.1-cli  
  
# Install composer and dependencies  
RUN apt-get update && apt-get install -y --no-install-recommends git
zlib1g-dev ca-certificates  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install mbstring  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename=composer  
  

