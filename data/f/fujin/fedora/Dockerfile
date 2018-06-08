FROM fedora:20  
MAINTAINER aj@junglistheavy.industries  
ENV container docker  
# Chef  
ADD https://www.opscode.com/chef/install.sh /install.sh  
RUN bash /install.sh  
# Packages  
RUN yum -y install systemd systemd-libs sudo openssh-server openssh-clients
curl  
# Update everything, purge systemd services.  
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
# OpenSSH Server Tweaks  
RUN sed -i '/UsePAM/d' /etc/ssh/sshd_config  
RUN echo 'UsePrivilegeSeparation no' >> /etc/ssh/sshd_config  
RUN echo 'UsePAM no' >> /etc/ssh/sshd_config  
RUN systemctl enable sshd  
  
VOLUME [ "/sys/fs/cgroup" ]  
ENTRYPOINT ["/usr/sbin/init"]  

