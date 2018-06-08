FROM centos:7  
MAINTAINER Chris Straffon <muppet_3000@hotmail.com>  
  
RUN yum update -y && yum install -y httpd mod_ssl openssl && yum clean all  
  
VOLUME ["/var/www/html","/etc/httpd/conf.d"]  
  
EXPOSE 80 443  
CMD /usr/sbin/httpd -D FOREGROUND  

