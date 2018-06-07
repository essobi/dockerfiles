FROM centos:7  
RUN yum -y update && \  
yum reinstall -y glibc-common && \  
yum clean all && \  
unlink /etc/localtime && \  
ln -s /usr/share/zoneinfo/Japan /etc/localtime && \  
rm -rf /var/log/*  
  
ENV LANG ja_JP.UTF-8  
ENV LANGUAGE ja_JP:ja  
ENV LC_ALL ja_JP.UTF-8

