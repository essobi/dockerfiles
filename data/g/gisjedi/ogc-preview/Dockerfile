FROM httpd:2.4  
ADD ./conf/geoserver.conf /usr/local/apache2/conf/extra/geoserver.conf  
ADD ./html/ogcpreview.tar.gz /usr/local/apache2/htdocs/  
RUN echo "Include conf/extra/geoserver.conf" >>
/usr/local/apache2/conf/httpd.conf  
RUN echo "LoadModule proxy_module modules/mod_proxy.so" >>
/usr/local/apache2/conf/httpd.conf  
RUN echo "LoadModule proxy_http_module modules/mod_proxy_http.so" >>
/usr/local/apache2/conf/httpd.conf  

