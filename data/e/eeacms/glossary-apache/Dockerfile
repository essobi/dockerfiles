FROM httpd:2.4  
MAINTAINER "Alin Voinea" <alin.voinea@eaudeweb.ro>  
  
RUN echo "Include conf/extra/virtual.conf" >>
/usr/local/apache2/conf/httpd.conf  
  
RUN sed -i 's|#LoadModule deflate_module|LoadModule deflate_module|'
/usr/local/apache2/conf/httpd.conf  
RUN sed -i 's|#LoadModule expires_module|LoadModule expires_module|'
/usr/local/apache2/conf/httpd.conf  
RUN sed -i 's|#LoadModule rewrite_module|LoadModule rewrite_module|'
/usr/local/apache2/conf/httpd.conf  
RUN sed -i 's|#LoadModule proxy_module|LoadModule proxy_module|'
/usr/local/apache2/conf/httpd.conf  
RUN sed -i 's|#LoadModule proxy_http_module|LoadModule proxy_http_module|'
/usr/local/apache2/conf/httpd.conf  
  
ADD vh-glossary.conf /usr/local/apache2/conf/extra/virtual.conf  

