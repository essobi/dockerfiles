#  
# CentOS 7 Dockerfile  
#  
# Build:  
# docker build -t zokeber/centos:latest .  
# Create:  
# docker create -it --name centos -h centos zokeber/centos  
# Start:  
# docker start centos  
# Connect with bash  
# docker exec -it centos bash  
# Pull base image  
FROM centos:latest  
  
# Maintener  
MAINTAINER Daniel Lopez Monagas <zokeber@gmail.com>  
  
# Update CentOS 7  
RUN yum update -y && yum upgrade -y  
  
# Install packages  
RUN yum install -y unzip wget curl git  
  
# Install EPEL Repository  
RUN yum install -y epel-release  
  
# Clean CentOS 7  
RUN yum clean all  
  
# Set the environment variables  
ENV HOME /root  
  
# Working directory  
WORKDIR /root  
  
# Default command  
CMD ["bash"]  

