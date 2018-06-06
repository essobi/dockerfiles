FROM composer:1  
MAINTAINER Irvin Capagcuan <irvin@capagcuan.org>  
  
COPY config/php.ini /usr/local/etc/php/  
  
RUN composer global require hirak/prestissimo \  
&& composer global require kherge/box=~2.7  
  
ENV PATH=$PATH:/tmp/vendor/bin  
  
VOLUME /app  
  
WORKDIR /app  
  
ENTRYPOINT ["box"]  

