FROM httpd:alpine  
RUN echo "Include conf/nilbus.com.conf" >> /usr/local/apache2/conf/httpd.conf  
COPY ./nilbus.com.conf /usr/local/apache2/conf/  
COPY ./pub/ /usr/local/apache2/htdocs/  

