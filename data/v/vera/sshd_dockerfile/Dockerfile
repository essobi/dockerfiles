FROM centos:7  
RUN yum update -y && yum install -y openssh-server openssh-clients.x86_64
rsync chkconfig coreutils curl findutils gawk glibc-common grep initscripts
lsof net-tools rpm shadow-utils tar util-linux which yum authconfig
policycoreutils-python  
  
RUN sed -i 's/#PermitRootLogin/PermitRootLogin/g' /etc/ssh/sshd_config  
RUN sed -i 's/#TCPKeepAlive/TCPKeepAlive/g' /etc/ssh/sshd_config  
RUN sed -i 's/#ClientAliveInterval 0/ClientAliveInterval 540/g'
/etc/ssh/sshd_config  
  
RUN ssh-keygen -A  
  
RUN /usr/sbin/sshd  

