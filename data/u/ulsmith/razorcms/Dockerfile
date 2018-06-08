FROM ulsmith/alpine-apache-php7  
MAINTAINER Paul Smith <pa.ulsmith.net>  
  
ADD ./ /app  
  
WORKDIR /app  
  
RUN composer install --no-dev  
  
RUN chown -R apache:apache /app  

