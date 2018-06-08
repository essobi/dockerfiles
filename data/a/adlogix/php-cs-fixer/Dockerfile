FROM php:7-alpine  
  
MAINTAINER Fred Cox "mcfedr@gmail.com"  
ENV PHP_CS_FIXER_VERSION v2.12.0  
RUN curl -L https://github.com/FriendsOfPHP/PHP-CS-
Fixer/releases/download/${PHP_CS_FIXER_VERSION}/php-cs-fixer.phar -o php-cs-
fixer \  
&& chmod +x php-cs-fixer \  
&& mv php-cs-fixer /usr/local/bin/php-cs-fixer  
  
CMD ["/usr/local/bin/php-cs-fixer", "fix"]  

