# sshd  
#  
# VERSION 0.1  
FROM vishy/centos  
MAINTAINER Vishwanath T K "vishwanath.tk@gmail.com"  
RUN yum -y update  
RUN yum -y install openssh-server openssh-clients  
RUN echo 'root:centos' |chpasswd  
RUN service sshd start  
  
RUN rm -f /etc/bashrc  
  
ADD files/color_prompt /etc/color_prompt  
ADD files/bashrc /etc/bashrc  
ADD files/.bashrc /root/.bashrc  
ADD files/.bash_profile /root/.bash_profile  
  
EXPOSE 22  
CMD /usr/sbin/sshd -D  

