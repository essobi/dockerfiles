FROM php:5.6-cli  
  
MAINTAINER Nick Jones <nick@nicksays.co.uk>  
  
RUN curl http://files.magerun.net/n98-magerun-latest.phar -o /n98-magerun.phar  
RUN chmod +x /n98-magerun.phar  
  
CMD [ "/n98-magerun.phar", "--root-dir=/var/www/html" ]  

