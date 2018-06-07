############################################################  
# Dockerfile to build latest CentOS 7  
############################################################  
# ideato:centos7-base  
# Set the base image to Ubuntu  
FROM centos:latest  
  
# File Author / Maintainer  
MAINTAINER Alessandro Mazzoli <am@ideato.it>  
  
ONBUILD RUN yum -y update  
  
# Install common packages  
RUN yum -y install vim \  
wget \  
curl \  
ntp  
  
## CentOS 7 and Red Hat (RHEL) 7 ##  
RUN wget https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && rpm -Uvh epel-release-latest-7.*.rpm  
RUN rpm -Uvh http://rpms.famillecollet.com/enterprise/remi-release-7.rpm  
  
# Setting timezone to Rome  
RUN unlink /etc/localtime  
RUN ln -s /usr/share/zoneinfo/Europe/Rome /etc/localtime  

