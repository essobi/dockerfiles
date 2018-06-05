FROM centos  
MAINTAINER Gavin  
RUN yum install httpd -y  
RUN echo 'Hello World!' > /var/www/html/index.html  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

