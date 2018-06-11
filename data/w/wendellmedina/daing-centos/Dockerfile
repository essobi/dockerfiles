# CentOS 7 custom build  
# https://github.com/wendellmedina/daing-centos  
#  
# Pull base image.  
FROM centos:centos7  
MAINTAINER Wendell Medina <wendellmedina@gmail.com>  
  
# Change timezone to SG  
RUN ln -sf /usr/share/zoneinfo/Asia/Singapore /etc/localtime  
  
# Update and install packages  
RUN yum update -y && \  
yum install -y curl sudo git vim && \  
yum clean all  

