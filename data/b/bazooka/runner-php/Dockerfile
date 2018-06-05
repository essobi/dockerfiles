FROM php:5.4-cli  
  
RUN apt-get update && apt-get install wget git mercurial subversion zlib1g-dev
-y  
  
RUN docker-php-ext-install zip  
RUN docker-php-ext-install mbstring  
  
RUN wget https://phar.phpunit.de/phpunit.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
  
RUN curl -sS https://getcomposer.org/installer | php -- --install-
dir=/usr/local/bin --filename composer  

