FROM centos:latest  
  
# Maintener  
MAINTAINER Erick Agrazal "erick.agrazal@gmail.com"  
RUN yum update -y && yum upgrade -y  
RUN yum install -y unzip wget curl git  
RUN yum install -y epel-release  
RUN yum clean all  
  
# Set the environment variables  
ENV HOME /root  
  
# Working directory  
WORKDIR /root  
  
# Default command  
CMD ["bash"]  

