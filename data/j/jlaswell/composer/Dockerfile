FROM php:7-alpine  
LABEL maintainer "John Laswell <john.n.laswell+github@gmail.com>"  
  
ADD install.sh /tmp  
RUN /tmp/install.sh \  
&& rm /tmp/install.sh  
  
USER www-data  
RUN composer global require hirak/prestissimo  
  
WORKDIR /app  
  
ENTRYPOINT ["/usr/local/bin/composer"]  

