# Base container for Holberton School  
#  
# Allow SSH connection to the container  
FROM ubuntu:14.04  
MAINTAINER Guillaume Salva <guillaume@holbertonschool.com>  
  
RUN apt-get update  
RUN apt-get -y upgrade  
  
# Install Vim and Emacs  
RUN apt-get install -y vim  
RUN apt-get install -y emacs  
  
# SSH  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/^#PasswordAuthentication/PasswordAuthentication/'
/etc/ssh/sshd_config  
RUN sed -ri 's/^PasswordAuthentication no/PasswordAuthentication yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
CMD ["/usr/sbin/sshd", "-D"]  

