FROM php:7.1.5-alpine  
  
ENTRYPOINT ["php-cs-fixer"]  
  
ENV COMPOSER_ALLOW_SUPERUSER "1"  
ENV COMPOSER_BIN_DIR "/usr/local/bin/"  
ENV COMPOSER_VENDOR_DIR "/usr/local/lib/composer/vendor/"  
RUN mkdir -p /usr/local/lib/composer/vendor/ && \  
php -r "copy('https://getcomposer.org/installer', 'composer-setup.php');" && \  
php -r "if (hash_file('SHA384', 'composer-setup.php') ===
'669656bab3166a7aff8a7506b8cb2d1c292f042046c5a994c43155c0be6190fa0355160742ab2e1c88d40d5be660b410')
{ echo 'Installer verified'; } else { echo 'Installer corrupt';
unlink('composer-setup.php'); } echo PHP_EOL;" && \  
php composer-setup.php --version 1.4.2 --install-dir=/usr/local/bin
--filename=composer && \  
php -r "unlink('composer-setup.php');" && \  
composer global require friendsofphp/php-cs-fixer:v2.3.1  

