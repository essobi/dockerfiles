FROM centos:7.4.1708  
LABEL osname="CentOS Linux"  
LABEL osversion="7.4"  
LABEL build-date="20180301"  
LABEL maintainer="Ferdinando Simonetti <ferdinando.simonetti@outlook.com>"  
# build-time proxy settings  
ARG MYPROXY  
ARG NOPROXY  
ENV http_proxy $MYPROXY  
ENV https_proxy $MYPROXY  
ENV no_proxy $NOPROXY  
ENV HTTP_PROXY $MYPROXY  
ENV HTTPS_PROXY $MYPROXY  
ENV NO_PROXY $NOPROXY  
  
RUN yum -y update && yum -y upgrade && \  
yum -y install https://dl.fedoraproject.org/pub/epel/epel-release-
latest-7.noarch.rpm && \  
rm -rf /var/cache/yum/*  
  
CMD ["/bin/bash"]  

