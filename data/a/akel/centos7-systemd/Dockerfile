FROM centos:7  
MAINTAINER "you" <your@email.here>  
  
ENV container docker  
  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
RUN yum -y update; yum clean all; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
RUN yum -y swap -- remove systemd-container systemd-container-libs -- install
systemd systemd-libs  
  
VOLUME [ "/sys/fs/cgroup" ]  
CMD ["/usr/sbin/init"]  

