FROM centos:latest  
MAINTAINER Esen Sagynov <kadishmal@gmail.com>  
  
# Update list of packages  
RUN yum update -y  
  
# Install OpenJDK 7 Runtime Environment  
RUN su -c "yum install -y java-1.7.0-openjdk"  
  
RUN yum clean all  

