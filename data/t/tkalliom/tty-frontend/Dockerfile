FROM httpd  
  
COPY ./web /usr/local/apache2/htdocs/  
RUN sed -i 's/Listen\ 80/Listen\ 3000/g' /usr/local/apache2/conf/httpd.conf  

