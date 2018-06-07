FROM centos:centos7  
MAINTAINER The CentOS Project <cloud-ops@centos.org>  
  
RUN yum update -y; yum clean all  
RUN yum -y install man; yum clean all  
ADD binfind /usr/src/binfind  
ADD testbin.sh /usr/src/testbin.sh  
RUN /usr/src/testbin.sh  

