FROM letsbonus/php-cli:7.0  
ENV MAX_OLD_IMAGES 3  
ENV REGISTRY_BASE_URI https://registry.letsbonus.net:5000  
COPY ./* /registry-gc/  
  
WORKDIR /registry-gc  
  
RUN COMPOSER_ALLOW_SUPERUSER=1 composer install -a --no-dev  
  
CMD ["php", "/registry-gc/gc.php"]  

