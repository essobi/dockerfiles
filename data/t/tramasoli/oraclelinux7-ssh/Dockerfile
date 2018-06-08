FROM oraclelinux:7  
MAINTAINER Fábio Tramasoli <fabio@tramasoli.com>  
LABEL env=des  
RUN yum -y install openssh-server shadow-utils  
RUN echo -e "ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key && ssh-keygen -t
dsa -f /etc/ssh/ssh_host_dsa_key && ssh-keygen -t ecdsa -f
/etc/ssh/ssh_host_ecdsa_key && echo \"root:hackme\" | chpasswd &&
/usr/sbin/sshd -D" > /bootstrap.sh  
EXPOSE 22  
CMD ["/bin/bash","/bootstrap.sh"]  

