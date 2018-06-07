#centos container for general purpose:  
FROM centos:latest  
MAINTAINER fugitivus <fugitivus@gmx.net>  
  
#install updates, some packages and do cleanup:  
RUN yum update -y && yum install net-tools -y\  
&& rm -rf /var/lib/{apt,dpkg,cache,log}/  

