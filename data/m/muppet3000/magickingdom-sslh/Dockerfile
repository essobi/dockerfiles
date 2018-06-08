FROM centos:7  
MAINTAINER Chris Straffon <muppet_3000@hotmail.com>  
  
RUN yum update -y && yum install -y epel-release && yum install -y sslh && yum
clean all  
  
COPY sslh.cfg /etc/sslh.cfg  
  
EXPOSE 443  
ENTRYPOINT sslh -F /etc/sslh.cfg  
  

