FROM php:7.1-apache  
  
ENV LANG C.UTF-8  
WORKDIR /app  
  
COPY config/php /usr/local/etc/php/conf.d  
  
COPY config/apache /etc/apache2/conf-enabled  
  
COPY bin /container-scripts  
  
RUN /container-scripts/prepare  
  
ENTRYPOINT ["/container-scripts/launch"]  

