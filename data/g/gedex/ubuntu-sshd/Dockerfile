FROM ubuntu:14.04  
MAINTAINER Akeda Bagus <admin@gedex.web.id>  
  
# Update packages and install openssh-server.  
RUN apt-get update  
RUN apt-get install -y openssh-server  
RUN mkdir /var/run/sshd  
  
# Set root password to 'root' and enable root login.  
RUN echo 'root:root' | chpasswd  
RUN sed -ri 's/^PermitRootLogin\s+.*/PermitRootLogin yes/'
/etc/ssh/sshd_config  
RUN sed -ri 's/UsePAM yes/#UsePAM yes/g' /etc/ssh/sshd_config  
  
EXPOSE 22  
ENTRYPOINT ["/usr/sbin/sshd"]  
CMD ["-D"]  

