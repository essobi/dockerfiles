FROM centos:centos6  
MAINTAINER FayeHuang  
RUN yum -y update && yum -y upgrade  
  
RUN yum -y install openssh-clients openssh-server \  
epel-release \  
vim && \  
yum clean all  
  
RUN rm -f /etc/ssh/ssh_host_dsa_key /etc/ssh/ssh_host_rsa_key && \  
ssh-keygen -q -N "" -t dsa -f /etc/ssh/ssh_host_dsa_key && \  
ssh-keygen -q -N "" -t rsa -f /etc/ssh/ssh_host_rsa_key  
  
# SSH login fix. Otherwise user is kicked off after login  
RUN sed -i '/pam_loginuid.so/c session optional pam_loginuid.so'
/etc/pam.d/sshd  
  
EXPOSE 22  
COPY ssh_init.sh /root/ssh_init.sh  
RUN chmod +x /root/ssh_init.sh  
CMD ./root/ssh_init.sh  

