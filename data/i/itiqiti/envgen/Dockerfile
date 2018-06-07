FROM php:7-alpine  
  
COPY . /app  
  
WORKDIR /app  
  
RUN curl -sS https://getcomposer.org/installer | php  
RUN php composer.phar --no-ansi -n install && \  
rm -f composer.phar  
  
CMD ["php", "bin/envgen", "generate", "/source", "/target"]  

