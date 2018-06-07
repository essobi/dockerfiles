FROM centos:centos7  
  
MAINTAINER Armen Kaleshian <armen@kriation.com>  
  
# Enable non-interactive installation by yum and update  
RUN sed -i 's/^\[main\]/\[main\]\nassumeyes = 1\nkeepcache = 0/'
/etc/yum.conf\  
&& yum update && yum clean all && rm -rf /var/cache/yum  

