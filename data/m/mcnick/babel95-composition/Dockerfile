FROM php:5.6-apache  
  
COPY . /src  
WORKDIR /src  
RUN php composer.phar install  
RUN cd /var/www && rm -rf html && ln -s /src/web html

