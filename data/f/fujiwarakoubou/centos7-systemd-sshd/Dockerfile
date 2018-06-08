FROM fujiwarakoubou/centos7-systemd  
  
RUN yum -y install openssh-server; yum clean all; systemctl enable
sshd.service  
  
CMD ["/usr/sbin/init"]

