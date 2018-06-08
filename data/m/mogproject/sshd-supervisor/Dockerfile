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
  
#  
# Supervisor  
#  
# enable EPEL repository  
RUN yum install -y --nogpgcheck
http://dl.iuscommunity.org/pub/ius/stable/Redhat/6/x86_64/epel-
release-6-5.noarch.rpm  
  
# install supervisord  
RUN yum install -y --nogpgcheck supervisor  
  
# settings  
ADD supervisord.conf /etc/supervisord.conf  
RUN mkdir -p /var/log/supervisor  
  
EXPOSE 22  
CMD ["/usr/bin/supervisord"]  

