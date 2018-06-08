FROM centos:7  
MAINTAINER lgu <freedomgll@163.com>  
  
RUN echo 'root:Welcome#1' | chpasswd  
  
RUN yum install -y openssh-server && yum install -y expect  
  
RUN mkdir /reworks  
  
ADD ssh_keygen.sh /reworks/ssh_keygen.sh  
  
RUN chmod a+x /reworks/ssh_keygen.sh  
  
RUN /reworks/ssh_keygen.sh  
  
EXPOSE 22  
CMD ["/usr/sbin/sshd", "-D"]

