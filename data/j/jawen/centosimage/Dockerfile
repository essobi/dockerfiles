FROM centos  
MAINTAINER jawen  
RUN yum install -y openssh-server && yum install -y sudo && yum install -y
net-tools && yum install -y vim && yum install -y openssh-clients && yum
install -y sshpass  
RUN echo "root:root" | chpasswd  
RUN echo "root ALL=(ALL) ALL" >> /etc/sudoers  
RUN ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key  
RUN sed -i 's/UsePAM yes/UsePAM no/g' /etc/ssh/sshd_config  
  
RUN mkdir /var/run/sshd  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]  
  

