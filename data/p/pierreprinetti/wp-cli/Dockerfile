FROM php:7-alpine  
  
ENV PAGER more  
  
RUN docker-php-ext-install mysqli  
  
RUN curl -O https://raw.githubusercontent.com/wp-cli/builds/gh-pages/phar/wp-
cli.phar  
  
RUN chmod +x wp-cli.phar && mv wp-cli.phar /bin/wp  
  
VOLUME /wordpress  
  
WORKDIR /wordpress  
  
CMD wp --allow-root  

