FROM centos:7  
MAINTAINER Feng Zhou <feng.zh@gmail.com>  
  
RUN yum install -y epel-release; yum install -y proftpd proftpd-ldap; yum
clean all  
  
CMD proftpd -n -q  

