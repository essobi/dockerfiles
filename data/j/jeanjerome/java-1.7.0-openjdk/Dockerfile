# Building a CentOS 6 image with OpenJDK 1.7  
FROM centos:6  
MAINTAINER Jean-Jerome Levy <contact@scalastic.io>  
  
# Install OpenJDK with yum and get things cleaned  
RUN yum update -y && \  
yum install -y java-1.7.0-openjdk-devel && \  
yum clean all -y  

