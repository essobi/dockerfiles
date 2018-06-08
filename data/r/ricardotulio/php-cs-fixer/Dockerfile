FROM php:7.2-cli-alpine  
  
RUN curl -L http://cs.sensiolabs.org/download/php-cs-fixer-v2.phar -o php-cs-
fixer && \  
chmod +x php-cs-fixer && \  
mv php-cs-fixer /usr/local/bin/  
  
ENTRYPOINT ["php", "-d", "memory_limit=-1", "/usr/local/bin/php-cs-fixer"]  

