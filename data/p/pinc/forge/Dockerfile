FROM ubuntu:16.04  
MAINTAINER Sam Smith <yo@samsmith.io>  
  
RUN apt-get update &&\  
apt-get install --yes kpartx qemu-user-static curl git binfmt-support iptables
&&\  
curl -sL https://deb.nodesource.com/setup_6.x | bash &&\  
apt-get install --yes nodejs  
  
RUN mkdir -p /opt/pinc/jenny  
COPY jenny /opt/pinc/jenny  
RUN cd /opt/pinc/jenny && npm install  
  
RUN mkdir -p /opt/pinc/forge/bin  
COPY forge /opt/pinc/forge/bin  
  
ENTRYPOINT ["/opt/pinc/forge/bin/forge"]  

