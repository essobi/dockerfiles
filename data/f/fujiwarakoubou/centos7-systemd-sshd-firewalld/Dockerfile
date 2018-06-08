FROM fujiwarakoubou/centos7-systemd-sshd  
  
RUN yum -y install firewalld; yum clean all; systemctl enable
firewalld.service  
  
CMD ["/usr/sbin/init"]

