FROM centos:7  
SHELL [ "bash", "-c" ]  
  
LABEL maintainer="Dana Dukes <drdukes@gmail.com>" \  
howtorun="Run with --cap-add=SYS_ADMIN option to allow xCAT to run under
systemd."  
  
ENV container docker  
  
ADD motd /etc/motd  
  
RUN (cd /lib/systemd/system/sysinit.target.wants/; for i in *; do [ $i == \  
systemd-tmpfiles-setup.service ] || rm -f $i; done); \  
rm -f /lib/systemd/system/multi-user.target.wants/* && \  
rm -f /etc/systemd/system/*.wants/* && \  
rm -f /lib/systemd/system/local-fs.target.wants/* && \  
rm -f /lib/systemd/system/sockets.target.wants/*udev* && \  
rm -f /lib/systemd/system/sockets.target.wants/*initctl* && \  
rm -f /lib/systemd/system/basic.target.wants:/* && \  
rm -f /lib/systemd/system/anaconda.target.wants/*  
  
RUN yum install -y \  
bind-utils \  
iproute \  
less \  
openssh-server \  
rsyslog \  
wget \  
yum-plugin-ovl && \  
yum clean all && \  
bash <( curl -L https://raw.githubusercontent.com/xcat2/xcat-core/master/xCAT-
server/share/xcat/tools/go-xcat ) --yes install && \  
sed -i -e 's|#PermitRootLogin yes|PermitRootLogin yes|g' \  
-e 's|#UseDNS yes|UseDNS no|g' /etc/ssh/sshd_config && \  
echo "root:cluster" | chpasswd && \  
touch /etc/NEEDINIT  
  
ADD entrypoint.sh /bin/entrypoint.sh  
  
RUN systemctl enable httpd && \  
systemctl enable sshd && \  
systemctl enable dhcpd && \  
systemctl enable rsyslog && \  
systemctl enable xcatd  
  
EXPOSE 80 22 22/udp 66 67 67/udp 68 68/udp 69 69/udp 53 53/udp 80 111 514 2049
20048 3001 3001/udp 3002 3002/udp 4011 33387 36995  
  
VOLUME [ "/install", "/tftpboot", "/var/log/xcat", "/sys/fs/cgroup" ]  
  
CMD [ "/usr/sbin/init", "entrypoint.sh" ]  

