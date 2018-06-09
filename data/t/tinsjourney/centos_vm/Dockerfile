FROM centos  
  
MAINTAINER Tinsjourney <tintin@gnali.org>  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/*;\  
rm -f /etc/systemd/system/*.wants/*;\  
rm -f /lib/systemd/system/local-fs.target.wants/*; \  
rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
rm -f /lib/systemd/system/basic.target.wants/*;\  
rm -f /lib/systemd/system/anaconda.target.wants/*;  
  
RUN yum -q -y --setopt="tsflags=nodocs" install openssh-server && \  
yum clean all && \  
rm -rf /var/cache/yum/*  
  
RUN /usr/sbin/sshd-keygen && \  
systemctl enable sshd  
  
VOLUME [ "/sys/fs/cgroup" ]  
  
CMD ["/usr/sbin/init"]  

