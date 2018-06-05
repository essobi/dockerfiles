FROM kaorimatz/systemd  
  
MAINTAINER Satoshi Matsumoto <kaorimatz@gmail.com>  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install bird && dnf clean all  
  
RUN systemctl enable bird  

