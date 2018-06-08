FROM centos:7  
MAINTAINER Oleksii Dzhulai  
  
RUN rpm -Uvh http://repos.mesosphere.io/el/7/noarch/RPMS/mesosphere-el-
repo-7-1.noarch.rpm  
RUN rpm -Uvh http://ftp.colocall.net/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
RUN yum -y update  
RUN yum -y install mesos chronos marathon mesosphere-zookeeper supervisor
selinux-policy-targeted docker lxc libselinux-python e2fsprogs  
  
RUN sed -ir /ulimit/d /usr/bin/marathon&&sed -ir /ulimit/d /usr/bin/chronos  
ADD wrap_docker_messos /bin/wrap_docker_messos  
RUN chmod +x /bin/wrap_docker_messos  
  
VOLUME /var/lib/docker  

