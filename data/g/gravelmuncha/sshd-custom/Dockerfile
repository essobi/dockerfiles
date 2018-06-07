FROM ubuntu  
  
MAINTAINER Raúl Sánchez <hola@raulsanchez.me>  
  
RUN apt update && apt install -y openssh-server  
  
RUN mkdir -p /var/run/sshd  
  
ADD sshd_config /etc/ssh/sshd_config  
  
CMD /usr/sbin/sshd -D  
  
EXPOSE 22  

