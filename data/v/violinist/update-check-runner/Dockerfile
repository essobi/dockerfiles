FROM drupaldocker/php:7.0-alpine-cli  
MAINTAINER eiriksm <eirik@morland.no>  
COPY . /usr/src/myapp  
WORKDIR /usr/src/myapp  
RUN composer install --no-dev --optimize-autoloader && composer global require
hirak/prestissimo  
CMD ["php", "runner.php"]  
  

