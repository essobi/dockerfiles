FROM centos:7  
  
MAINTAINER CSA Data Group <csa-data-group@wuxinextcode.com>  
  
# Dependencies for Tertiary Pipeline's Makefile and Dockerfile  
RUN yum -y upgrade && \  
yum -y groupinstall "Development tools" && \  
yum -y install which wget yum-utils && \  
yum-config-manager --add-repo \  
https://download.docker.com/linux/centos/docker-ce.repo && \  
yum makecache fast && \  
yum -y install docker-ce && \  
yum -y clean all  

