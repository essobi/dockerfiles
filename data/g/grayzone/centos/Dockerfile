FROM centos:latest  
  
MAINTAINER Albert Wang  
  
ENV container docker  
  
RUN echo "root:123456" | chpasswd  
  
RUN yum -y install sudo epel-release && yum clean all  
RUN yum -y update && yum clean all  
  
CMD ["/usr/sbin/init"]

