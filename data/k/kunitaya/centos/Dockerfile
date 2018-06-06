#  
# CentOS with ja_JP  
# kunitaya/centos  
#  
# 2017-04-24  
# CentOS Linux 7.3.1611  
FROM centos  
MAINTAINER kunitaya  
  
RUN yum makecache fast  
RUN yum -y update  
RUN yum -y reinstall glibc-common  
RUN yum clean all  
RUN localedef -v -c -i ja_JP -f UTF-8 ja_JP.UTF-8; echo "";  
  
env LANG=ja_JP.UTF-8  
RUN rm -f /etc/localtime  
RUN ln -fs /usr/share/zoneinfo/Asia/Tokyo /etc/localtime  

