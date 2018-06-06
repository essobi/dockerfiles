FROM alpine  
MAINTAINER kgoutsos  
  
# Getting packages  
RUN apk add --no-cache --update bash openssh net-tools python curl  
  
# Installing the startup script that initialises the SSH server  
ADD entrypoint.sh /root/  
  
# Commands to run at container startup  
ENTRYPOINT ["/root/entrypoint.sh"]  
CMD ["/usr/sbin/sshd","-D"]  

