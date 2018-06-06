FROM centos  
MAINTAINER Xing James Jiang  
RUN yum install httpd -y  
RUN echo 'Cisco Switch 2016' > /var/www/html/index.html  
EXPOSE 80  
CMD ["/usr/sbin/httpd","-D","FOREGROUND"]  

