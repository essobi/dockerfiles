FROM php:7.2.3-fpm  
  
RUN apt-get update -y \  
&& apt-get install -y libxml2-dev libicu-dev zlib1g-dev mysql-client git
openssh-client \  
&& docker-php-source extract \  
&& docker-php-ext-install zip mbstring dom bcmath intl pdo_mysql \  
&& docker-php-source delete  
  
RUN curl -OL
https://github.com/jwilder/dockerize/releases/download/v0.6.0/dockerize-linux-
amd64-v0.6.0.tar.gz && tar \--skip-old-files -C /usr/local/bin -xzvf
dockerize-linux-amd64-v0.6.0.tar.gz && rm dockerize-linux-amd64-v0.6.0.tar.gz  
# Install Composer and make it available in the PATH  
RUN curl -sS https://getcomposer.org/installer | php \-- --install-
dir=/usr/bin/ --filename=composer  

