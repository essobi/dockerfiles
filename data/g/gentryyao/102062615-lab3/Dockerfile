FROM httpd:2.4  
MAINTAINER Gentry Yaoo <polo90406@gamil.com>  
  
RUN sed -i 's/Listen 80/Listen 5566/g' /usr/local/apache2/conf/httpd.conf  
RUN sed -i 's/#ServerName www\\.example\\.com:80/ServerName localhost:5566/g'
/usr/local/apache2/conf/httpd.conf  
  
EXPOSE 5566  

