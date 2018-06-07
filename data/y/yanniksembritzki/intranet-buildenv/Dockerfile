FROM php:latest  
RUN apt-get update \  
&& apt-get install -y zlib1g-dev libsqlite3-dev \  
&& docker-php-ext-install -j$(nproc) zip pdo_sqlite \  
&& apt-get install -y \--no-install-recommends git \  
&& curl \--silent
https://raw.githubusercontent.com/composer/getcomposer.org/453523e8e9b093bfc02b49b723bf0149888d98c1/web/installer
| php -- --quiet --install-dir=/usr/local/bin --filename=composer \  
&& composer global require "hirak/prestissimo:^0.3" \  
&& docker-php-source delete \  
&& rm -rf /var/log/*; rm -rf /tmp/*; rm -rf /var/lib/apt/lists/*  

