FROM ubuntu:17.04  
RUN apt-get update && \  
apt-get install -y virt-manager openssh-client ssh-askpass && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN adduser root libvirt  
  
ADD launch.sh /root/  
RUN chmod +x /root/launch.sh  

