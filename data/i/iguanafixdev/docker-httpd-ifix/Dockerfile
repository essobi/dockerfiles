FROM httpd:2.2  
  
RUN apt-get update && apt-get install -y vim  
RUN mkdir /usr/local/apache2/conf/ssl  
RUN mkdir /webapp  
  
COPY ./conf/ssl /usr/local/apache2/conf/ssl  
COPY ./conf/httpd.conf /usr/local/apache2/conf/httpd.conf  
COPY ./conf/iguana-core.conf /usr/local/apache2/conf/iguana-core.conf  

