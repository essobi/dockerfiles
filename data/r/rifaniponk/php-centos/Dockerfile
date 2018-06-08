##################################################  
# Centos 7 server for php application development  
###################################################  
# Base image is centos 7  
FROM centos:7  
# Author: Rifan  
MAINTAINER Rifan MF <rifan.refun@gmail.com>  
  
RUN yum -y update && yum clean all  
  
# install httpd  
RUN yum -y install httpd  
  
# install supervisor  
RUN yum -y install python-setuptools  
RUN easy_install supervisor  
  
RUN yum clean all  

