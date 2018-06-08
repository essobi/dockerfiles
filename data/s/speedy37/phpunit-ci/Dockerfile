FROM php:5.6  
  
RUN apt-get update -yqq \  
&& apt-get install git -yqq \  
&& curl -L https://phar.phpunit.de/phpunit.phar > /usr/local/bin/phpunit \  
&& chmod +x /usr/local/bin/phpunit  

