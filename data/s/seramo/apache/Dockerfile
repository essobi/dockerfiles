FROM httpd:alpine  
MAINTAINER Seramo <hello@seramo.com>  
  
RUN apk --no-cache add shadow  
RUN usermod -u 1000 www-data  
  
COPY seramo.conf /usr/local/apache2/conf/seramo.conf  
  
RUN echo "Include conf/seramo.conf" >> /usr/local/apache2/conf/httpd.conf  
  
VOLUME /web  
VOLUME /logs  

