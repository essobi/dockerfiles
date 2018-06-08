FROM centos  
MAINTAINER adam  
RUN yum install httpd -y; yum clean all  
RUN echo 'Hello, world' > /var/www/html/index.html  
EXPOSE 80 443  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

