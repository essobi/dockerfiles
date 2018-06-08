# "ported" from https://github.com/CentOS/CentOS-Dockerfiles  
FROM centos:centos7  
MAINTAINER Ritesh Khadgaray <ritesh.a.khadgaray@accenture.com>  
  
RUN yum -y update; yum clean all  
RUN yum -y install java-1.8.0-openjdk-devel.x86_64 && yum clean all  
  
# cleanup old files  
RUN rm -rf /var/cache/yum /var/tmp/* /tmp/* /var/log/*  
  
CMD ["/bin/bash"]  
  

