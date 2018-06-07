# 20180602  
FROM oraclelinux:7  
MAINTAINER Todd Vierling <tv@duh.org>  
  
RUN rpm --rebuilddb && yum update -y && yum install -y sudo && yum clean all
&& rm -rf /var/cache/yum/*  

