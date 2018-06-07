FROM centos  
MAINTAINER j.ishiguro  
  
RUN yum update -y  
RUN yum install -y httpd  
RUN yum clean all  
ADD ./site2/ /var/www/html/  
  
EXPOSE 80  
CMD ["/usr/sbin/httpd", "-D", "FOREGROUND"]

