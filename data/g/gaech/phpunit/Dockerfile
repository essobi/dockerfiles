FROM php:5.6.30-alpine  
  
RUN curl -o phpunit.phar https://phar.phpunit.de/phpunit-4.6.6.phar  
RUN chmod +x phpunit.phar  
RUN mv phpunit.phar /usr/local/bin/phpunit  
RUN phpunit --version  

