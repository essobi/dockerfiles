FROM ubuntu:16.04  
MAINTAINER moremagic <itoumagic@gmail.com>  
  
RUN apt-get update && apt-get install -y openssh-server openssh-client  
RUN mkdir /var/run/sshd  
RUN echo 'root:root' | chpasswd  
RUN sed -i 's/PermitRootLogin .*$/PermitRootLogin yes/' /etc/ssh/sshd_config  
RUN sed -i 's/Port 22$/Port 23/' /etc/ssh/sshd_config  
  
EXPOSE 23  
CMD ["/usr/sbin/sshd", "-D"]  
  

