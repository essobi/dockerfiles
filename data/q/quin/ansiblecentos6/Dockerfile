FROM centos:6  
MAINTAINER quin  
  
RUN yum -y update \  
&& yum -y install epel-release  
  
RUN yum -y install \  
ansible \  
tar \  
unzip  
  
RUN yum -y remove epel-release && \  
yum clean all  

