FROM kaorimatz/systemd  
  
MAINTAINER Satoshi Matsumoto <kaorimatz@gmail.com>  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install unbound && dnf clean all  
  
RUN systemctl enable unbound  
  
EXPOSE 53/udp  

