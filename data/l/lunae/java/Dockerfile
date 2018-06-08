#################################################  
# Dockerfile for creating a Fedora 21 based Java  
# environment that includes the following :  
# - Maven  
# - OpenJDK 1.7  
#################################################  
  
# Set base image  
FROM fedora:21  
  
# Author / Maintainer  
MAINTAINER Emmanuel Luna  
  
# Run updates, install OpenJDK 1.7  
RUN yum update -y && \  
yum install java-1.8.0-openjdk maven -y && \  
yum clean all  

