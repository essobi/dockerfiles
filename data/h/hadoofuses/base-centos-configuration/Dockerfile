FROM centos:7.4.1708  
MAINTAINER Josiah Berkebile <praenato14@gmail.com>  
  
RUN yum update -y  
RUN yum -y install openssh-server passwd sudo  
RUN yum clean all  
RUN ssh-keygen -A  
RUN useradd ansible && usermod -aG wheel ansible  
RUN echo 'ansible:ansible' | chpasswd  
  
EXPOSE 22  
ENTRYPOINT ["/usr/sbin/sshd", "-D"]  

