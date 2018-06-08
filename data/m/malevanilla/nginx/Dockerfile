# Version 0.0.1  
FROM centos:7  
MAINTAINER Alan Chu "malevanilla@gmail.com"  
ENV WEB_DOCUMENT_ROOT /srv/www  
ENV WEB_DOCUMENT_INDEX index.php  
  
COPY conf/nginx.repo /etc/yum.repos.d/  
  
RUN yum update -y  
RUN yum install -y nginx  
  
COPY conf/www.conf /etc/ngninx/conf.d/  
  
EXPOSE 80 443  

