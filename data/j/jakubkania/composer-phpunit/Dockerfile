FROM php:5.6  
  
RUN apt-get update \  
&& apt-get install -qq \  
git \  
unzip \  
phpunit \  
&& curl --silent --show-error https://getcomposer.org/installer | php \  
&& mv composer.phar /usr/bin/composer \  
&& apt-get clean \  
&& rm -rf /var/lib/apt/lists/*  

