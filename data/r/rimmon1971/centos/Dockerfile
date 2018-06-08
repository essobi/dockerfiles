FROM centos:7.4.1708  
MAINTAINER ferdinando.simonetti@outlook.com  
  
# build-time proxy settings  
ARG MYPROXY  
ARG NOPROXY  
ENV http_proxy $MYPROXY  
ENV https_proxy $MYPROXY  
ENV no_proxy $NOPROXY  
ENV HTTP_PROXY $MYPROXY  
ENV HTTPS_PROXY $MYPROXY  
ENV NO_PROXY $NOPROXY  
# static copy of EPEL repos  
COPY epel-release-latest-7.noarch.rpm /  
# install EPEL and updates  
RUN yum -y update && \  
yum -y localinstall /epel-release-latest-7.noarch.rpm && \  
yum -y \--disablerepo=epel upgrade ca-certificates && \  
yum -y update && \  
yum -y clean all  

