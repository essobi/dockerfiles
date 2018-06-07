FROM centos:centos6  
  
MAINTAINER George Niculae <george.niculae79@gmail.com>  
  
RUN yum update -y  
  
# install utilities  
RUN yum install -y wget \  
openssh-server \  
openssh-clients  
  
# configure ssh  
RUN mkdir /var/run/sshd && \  
echo 'root:admin' | chpasswd && \  
sed -i 's/PermitRootLogin without-password/PermitRootLogin yes/'
/etc/ssh/sshd_config && \  
sed 's@session\s*required\s*pam_loginuid.so@session optional
pam_loginuid.so@g' -i /etc/pam.d/sshd && \  
/usr/bin/ssh-keygen -q -t rsa -f /etc/ssh/ssh_host_rsa_key -C '' -N '' && \  
/usr/bin/ssh-keygen -q -t dsa -f /etc/ssh/ssh_host_dsa_key -C '' -N ''  
  
# install sipxcom  
RUN wget -P /etc/yum.repos.d
http://download.sipxcom.org/pub/sipXecs/15.08/sipxecs-15.08.0-centos.repo  
RUN yum install -y sipxecs  
  
ENTRYPOINT ["/bin/bash"]  

