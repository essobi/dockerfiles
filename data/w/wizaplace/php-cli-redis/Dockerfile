FROM php:7.2-cli  
  
RUN apt-get update \  
&& apt-get install -y libicu-dev \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/* \  
&& docker-php-ext-install intl \  
&& pecl install redis \  
&& docker-php-ext-enable redis  

