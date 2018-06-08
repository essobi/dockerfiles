FROM centos:6.4  
#  
# SSH  
#  
RUN yum install -y --nogpgcheck openssh-server sudo  
RUN ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key && ssh-keygen -t dsa -f
/etc/ssh/ssh_host_dsa_key && sed -i 's/UsePAM.*/UsePAM no/g'
/etc/ssh/sshd_config  
  
# create user  
RUN useradd ssh-user && echo 'ssh-user:ssh-user' | chpasswd && echo 'ssh-user
ALL=(ALL) NOPASSWD:ALL' >> /etc/sudoers  
  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

