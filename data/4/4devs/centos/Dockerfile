FROM centos:centos7  
  
RUN yum -y --setopt=tsflags=nodocs install deltarpm vim git htop
http://rpms.famillecollet.com/enterprise/remi-release-7.rpm \  
&& yum-config-manager --enable remi \  
&& yum update -y \  
&& yum clean all  
  
RUN export TERM='xterm-256color'  

