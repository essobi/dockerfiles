  
FROM centos:latest  
MAINTAINER Oleksandr Shevchenko <mr.AlexZT@gmail.com>  
  
RUN yum install -y epel-release  
RUN yum update -y && yum upgrade -y  
RUN yum install -y git mc wget tar htop bash-completion  
  
RUN cd /usr/src ; git clone https://github.com/letsencrypt/letsencrypt && cd
letsencrypt  

