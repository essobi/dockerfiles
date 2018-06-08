FROM centos:latest  
MAINTAINER Yasser B. <boukhersy@gmail.com>  
  
# Install Python3 & Nodejs 8.  
RUN \  
yum -y -q -e 0 install https://centos7.iuscommunity.org/ius-release.rpm && \  
yum -y -q -e 0 install python36u && \  
yum -y -q -e 0 install python36u-pip &&\  
curl --silent \--location https://rpm.nodesource.com/setup_8.x | bash - && \  
yum -y -q -e 0 install nodejs && \  
yum -y -q -e 0 install gcc-c++ make git  

