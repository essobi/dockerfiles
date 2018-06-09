FROM centos  
  
RUN yum -y update  
RUN yum -y install httpd  
  
RUN echo "hello docker" > /var/www/html/index.html  
  
EXPOSE 80  
CMD /usr/sbin/apachectl -D FOREGROUND  

