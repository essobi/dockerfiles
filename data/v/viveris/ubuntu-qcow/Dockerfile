FROM ubuntu:16.04  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y libguestfs-tools qemu-utils
sshpass && \  
apt-get clean && \  
apt-get autoclean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  

