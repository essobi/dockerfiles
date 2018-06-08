FROM centos  
MAINTAINER John  
RUN yum install httpd -y  
RUN yum clean all  
RUN echo 'docker file auto build v1' > /var/www/html/index.html  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

