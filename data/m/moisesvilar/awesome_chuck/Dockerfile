FROM moisesvilar/apache_php:alpine3.3  
MAINTAINER Moisés Vilar  
  
RUN mkdir /var/www/localhost/htdocs/chuck  
ADD index.php /var/www/localhost/htdocs/chuck  
  
EXPOSE 80  
CMD httpd -D FOREGROUND

