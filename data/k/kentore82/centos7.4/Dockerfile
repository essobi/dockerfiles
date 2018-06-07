  
#RUN mkdir /var/run/sshd  
#RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ''  
#RUN echo 'root' |passwd root --stdin  
#ENTRYPOINT ["/usr/sbin/sshd", "-D"]  
###########  
FROM centos:7.4.1708  
MAINTAINER Ken Tore Tallakstad <tallakstad@gmail.com>  
  
ENV container docker  
  
RUN yum -y update; yum clean all  
  
RUN yum -y swap -- remove systemd-container systemd-container-libs -- install
systemd systemd-libs dbus fsck.ext4 passwd sudo vim initscripts  
  
RUN yum clean all  
  
ADD ./start.sh /start.sh  
  
RUN systemctl mask dev-mqueue.mount dev-hugepages.mount \  
systemd-remount-fs.service sys-kernel-config.mount \  
sys-kernel-debug.mount sys-fs-fuse-connections.mount \  
display-manager.service graphical.target systemd-logind.service  
  
#RUN yum -y swap -- remove fakesystemd -- install systemd systemd-libs  
#RUN yum -y update; yum clean all; \  
#(cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i ==
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
#rm -f /lib/systemd/system/multi-user.target.wants/*;\  
#rm -f /etc/systemd/system/*.wants/*;\  
#rm -f /lib/systemd/system/local-fs.target.wants/*; \  
#rm -f /lib/systemd/system/sockets.target.wants/*udev*; \  
#rm -f /lib/systemd/system/sockets.target.wants/*initctl*; \  
#rm -f /lib/systemd/system/basic.target.wants/*;\  
#rm -f /lib/systemd/system/anaconda.target.wants/*;  
RUN yum -y install openssh-server sudo openssh-clients  
RUN sed -i 's/#PermitRootLogin no/PermitRootLogin yes/' /etc/ssh/sshd_config  
  
# set UseDNS=no so avooid slow ssh login  
RUN sed -i 's/#UseDNS yes/UseDNS no/' /etc/ssh/sshd_config  
  
RUN ssh-keygen -q -f /etc/ssh/ssh_host_rsa_key -N '' -t rsa && \  
ssh-keygen -q -f /etc/ssh/ssh_host_ecdsa_key -N '' -t ecdsa && \  
ssh-keygen -q -f /etc/ssh/ssh_host_ed25519_key -N '' -t ed25519  
RUN echo 'root:root' | chpasswd  
  
# emable dbus, hostname, sshd service  
ADD dbus.service /etc/systemd/system/dbus.service  
RUN systemctl enable dbus.service  
RUN systemctl enable systemd-hostnamed.service  
RUN systemctl enable sshd.service  
  
VOLUME [ "/sys/fs/cgroup" ]  
VOLUME ["/run"]  
  
RUN chmod 755 /start.sh  
RUN ./start.sh  
  
# expose ssh system port  
EXPOSE 22  
CMD ["/usr/sbin/init"]  

