#  
# Author: Rohith  
# Date: 2015-08-16 11:39:24 +0100 (Sun, 16 Aug 2015)  
#  
# vim:ts=2:sw=2:et  
#  
FROM centos  
MAINTAINER Rohith <gambol99@gmail.com>  
  
ENV container docker  
RUN yum --setopt=tsflags=nodocs -y update && \  
yum --setopt=tsflags=nodocs -y install wget && \  
yum --setopt=tsflags=nodocs -y install nfs-utils && \  
yum -y swap -- remove fakesystemd -- install systemd systemd-libs && \  
yum update -y systemd-container  
  
RUN yum -y update; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
rm -f /etc/sysconfig/network-scripts/ifcfg-ens3;  
  
ADD config/ifcfg-eth0 /etc/sysconfig/network-scripts/ifcfg-eth0  
  
RUN wget
http://download.gluster.org/pub/gluster/glusterfs/3.7/3.7.3/CentOS/glusterfs-
epel.repo -O /etc/yum.repos.d/glusterfs-epel.repo  
RUN rpm -Uvh http://dl.fedoraproject.org/pub/epel/7/x86_64/e/epel-
release-7-5.noarch.rpm  
  
RUN yum --setopt=tsflags=nodocs -y install glusterfs glusterfs-server
glusterfs-fuse glusterfs-geo-replication glusterfs-cli glusterfs-api && \  
yum --setopt=tsflags=nodocs -y install attr iputils iproute nfs-common && \  
yum clean all  
  
VOLUME [ "/sys/fs/cgroup" ]  
  
EXPOSE 111 245 24007 24008 24009 2049 6010 6011 6012 38465 38466 38468 38469
49152 49153 49154 49156 49157 49158 49159 49160 49161 49162  
  
RUN systemctl disable nfs-server.service  
RUN systemctl enable rpcbind.service  
RUN systemctl enable glusterd.service  
  
CMD ["/usr/sbin/init"]  

