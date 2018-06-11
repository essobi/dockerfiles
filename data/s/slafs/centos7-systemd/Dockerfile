# based on work in https://github.com/maci0/docker-systemd-unpriv  
FROM centos:centos7  
  
MAINTAINER slafs  
  
ENV container docker  
  
RUN yum -y update  
  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
  
RUN yum clean all  
  
RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \  
systemd-remount-fs.service sys-kernel-config.mount \  
sys-kernel-debug.mount sys-fs-fuse-connections.mount  
  
RUN systemctl mask display-manager.service systemd-logind.service  
  
RUN systemctl disable graphical.target; systemctl enable multi-user.target  
  
ADD dbus.service /etc/systemd/system/dbus.service  
  
VOLUME ["/sys/fs/cgroup"]  
  
VOLUME ["/run"]  
  
CMD ["/usr/lib/systemd/systemd"]  

