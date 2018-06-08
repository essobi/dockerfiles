FROM roneichiarandi/php:7.1-cli  
  
# Install Composer  
RUN php /tmp/composer-setup.php --no-ansi --install-dir=/usr/local/bin
--filename=composer --snapshot && rm -rf /tmp/composer-setup.php  
  
RUN wget -c http://static.phpmd.org/php/latest/phpmd.phar && chmod +x
phpmd.phar; \  
mv phpmd.phar /usr/local/bin/phpmd; \  
phpmd --version  
  
RUN curl -OL https://squizlabs.github.io/PHP_CodeSniffer/phpcs.phar && chmod
+x phpcs.phar; \  
mv phpcs.phar /usr/local/bin/phpcs; \  
phpcs -h  
  
RUN composer global require phpunit/phpunit:*  
  
WORKDIR /app  

