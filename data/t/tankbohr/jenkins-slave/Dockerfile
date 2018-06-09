FROM centos:latest  
MAINTAINER Alexey Niktin <niktin@corp.sputnik.ru>  
  
RUN yum install -y openssh-server rsyslog java-1.7.0-openjdk subversion git
boost icu wget vim  
# Adds user jenkins with password jenkins  
RUN useradd -G root --password `openssl passwd -crypt jenkins` jenkins  
  
RUN chkconfig sshd on  
RUN service sshd start  
RUN service sshd stop  
  
EXPOSE 22  
  

