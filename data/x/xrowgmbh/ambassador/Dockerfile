FROM centos:centos7  
  
MAINTAINER "Björn Dieding" <bjoern@xrow.de>  
  
ENV container=docker  
  
RUN yum -y update; yum clean all  
RUN yum -y install socat; yum clean all  
  
CMD env | grep AMBASSADOR= | sed 's/AMBASSADOR=tcp:\/\/\\(.*\\):\\(.*\\)/socat
-t 100000000 TCP4-LISTEN:\2,fork,reuseaddr TCP4:\1:\2 \& wait/' | sh  

