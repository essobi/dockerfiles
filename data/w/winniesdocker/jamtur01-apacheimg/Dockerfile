FROM ubuntu:latest  
MAINTAINER James Turnbull "james@example.com"  
#RUN apt-get update  
#RUN apt-get install -y httpd httpd-devel  
ENV APACHE_RUN_USER www-data  
ENV APACHE_RUN_DIR /var/log/apache2  
ONBUILD ADD ./var/www/  
ONBUILD ADD ./usr/sbin/apache2  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/apache2"]  
  
CMD ["-D","FOREGROUND"]  
  

