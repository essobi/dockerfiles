FROM centos:7  
MAINTAINER witsec <mark@witsec.nl>  
  
RUN yum update -y && \  
yum install -y php php-pgsql httpd && \  
yum clean all  
  
COPY app/* /var/www/html/  
  
EXPOSE 80  
ENTRYPOINT ["/usr/sbin/httpd"]  
CMD ["-D", "FOREGROUND"]  

