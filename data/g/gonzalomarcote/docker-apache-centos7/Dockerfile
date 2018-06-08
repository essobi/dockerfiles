# Version: 0.0.1 - Docker image with a minimal installation of apache and
Centos7 64bits  
FROM centos:latest  
MAINTAINER Gonzalo Marcote "gonzalomarcote@gmail.com"  
RUN yum -y update  
RUN yum -y install yum-plugin-priorities yum-plugin-fastestmirror  
RUN yum -y install vim tar  
RUN yum -y install httpd  
EXPOSE 80 8080  

