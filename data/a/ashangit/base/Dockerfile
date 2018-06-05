#  
# Centos base  
#  
# Pull base image.  
FROM centos:7  
MAINTAINER Nicolas Fraison <nfraison@yahoo.fr>  
  
ENV EPEL_VERSION latest-7  
# Add tooling and Epel  
RUN yum install -y wget tar net-tools && \  
yum clean all  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-
release-${EPEL_VERSION}.noarch.rpm && \  
rpm -ivh epel-release-${EPEL_VERSION}.noarch.rpm && \  
rm -f epel-release-${EPEL_VERSION}.noarch.rpm  
  
# Create defaults apps & data folder  
RUN mkdir -p /apps /data  
  
ONBUILD RUN yum update -y  
  
# Define working directory.  
WORKDIR /data  
  
# Define default command.  
CMD /bin/bash

