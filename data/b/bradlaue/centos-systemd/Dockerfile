FROM centos:centos7  
MAINTAINER "Brad Laue" <brad@brad-x.com>  
  
RUN yum -y update; yum clean all; \  
yum -y swap -- remove fakesystemd -- install systemd systemd-libs; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*; \  
systemctl mask getty.target swap.target && systemctl disable graphical.target;
systemctl enable multi-user.target  
  
VOLUME ["/sys/fs/cgroup"]  
VOLUME ["/run"]  
VOLUME ["/export"]  
  
ENV container lxc  
CMD ["/usr/lib/systemd/systemd"]  

