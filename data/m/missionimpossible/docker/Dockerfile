FROM centos:latest  
MAINTAINER Viral Makwana  
EXPOSE 80  
RUN yum install httpd -y  
ADD index.html /var/www/html/index.html  
ADD 001-dockertest.conf /etc/httpd/conf.d/001-dockertest.conf  
CMD /usr/sbin/httpd -DFOREGROUND  

