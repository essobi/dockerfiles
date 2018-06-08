FROM centos:7  
MAINTAINER Aman Mangal <mangalaman93@gmail.com>  
  
ENV MESOS_SYSTEMD_ENABLE_SUPPORT=false  
  
RUN yum -y --setopt=tsflags=nodocs install libtool-ltdl && \  
yum clean all  
  
RUN rpm -Uvh http://repos.mesosphere.com/el/7/noarch/RPMS/mesosphere-el-
repo-7-1.noarch.rpm && \  
yum -y install mesos && \  
yum clean all  

