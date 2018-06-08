FROM httpd:alpine  
MAINTAINER Seramo <hello@seramo.com>  
  
RUN mkdir /web && chown -R www-data:www-data /web  
RUN mkdir /logs && chown -R www-data:www-data /logs  
  
COPY seramo.conf /usr/local/apache2/conf/seramo.conf  
  
RUN echo "Include conf/seramo.conf" >> /usr/local/apache2/conf/httpd.conf  
  
VOLUME /web  
VOLUME /logs  

