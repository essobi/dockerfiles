FROM centos:6.6  
COPY httpd-foreground /usr/local/bin/  
  
RUN yum --nogpgcheck update -y  
RUN yum --nogpgcheck install -y deltarpm gd gd-devel php php-mysql php-gd  
RUN chmod 775 /usr/local/bin/httpd-foreground  
  
EXPOSE 80  
CMD ["httpd-foreground"]  

