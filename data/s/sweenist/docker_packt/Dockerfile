FROM ubuntu:trusty  
  
MAINTAINER Ryan Sweeney <sween119@hotmail.com>  
  
RUN apt-get update && apt-get install -y openssh-server  
RUN mkdir -p /var/run/sshd  
ONBUILD ADD sshd_config /etc/ssh/sshd_config  
  
CMD /usr/sbin/sshd -D  
  
EXPOSE 2222  

