FROM centos  
MAINTAINER RevieReyes  
RUN yum update -y && yum install httpd -y && yum install php -y  
ADD info.php /var/www/html  
EXPOSE 80  
VOLUME ["/sys/fs/cgroup","/var/www/html"]  
CMD ["httpd","-D","FOREGROUND"]  

