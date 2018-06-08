FROM centos:6  
EXPOSE 80  
RUN yum clean all; yum -y install apache php php-pdo sqlite php-mysql  
ENTRYPOINT ["/usr/sbin/httpd", "-D", "FOREGROUND"]  

