FROM kaorimatz/systemd  
  
MAINTAINER Satoshi Matsumoto <kaorimatz@gmail.com>  
  
RUN dnf -y update && dnf clean all  
RUN dnf -y install trafficserver && dnf clean all  
  
RUN systemctl enable trafficserver  
  
EXPOSE 8080  

