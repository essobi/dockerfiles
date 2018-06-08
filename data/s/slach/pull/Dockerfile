#  
# Dockerfile  
#  
FROM centos:centos7  
MAINTAINER Sebastian Lach <root@slach.eu>  
  
# define environment  
ENV LANG=en_US.UTF-8 LC_ALL=en_US.UTF-8  
# install dependencies  
RUN yum clean all && yum -y update && \  
yum -y install epel-release && \  
yum -y install ansible git openssh-clients  
  
# install systemd  
RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs; \  
(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == systemd-
tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*; \  
rm -f /etc/systemd/system/*.wants/*; \  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*; \  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
# generate ssh keys  
RUN ssh-keygen -q -t rsa -f ~/.ssh/id_rsa  
  
# configure systemd  
ADD pull.service /etc/systemd/system/pull.service  
RUN systemctl enable pull  
  
# container's entrypoint  
VOLUME ["/etc/pull.conf"]  
ENTRYPOINT ["/sbin/init"]  
  

