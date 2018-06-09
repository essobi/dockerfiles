FROM debian:9  
  
LABEL maintainer="simon@widgit.com"  
  
ENV DEBIAN_FRONTEND=noninteractive  
  
RUN apt-get -y update && \  
apt-get -y install wget build-essential xorg net-tools && \  
wget -O /tmp/vmware-install.bundle.tar \  
https://softwareupdate.vmware.com/cds/vmw-
desktop/ws/12.5.8/7098237/linux/core/VMware-
Workstation-12.5.8-7098237.x86_64.bundle.tar && \  
tar xvf /tmp/vmware-install.bundle.tar -C /tmp && \  
mv /tmp/*.bundle /tmp/vmware-install.bundle && \  
chmod +x /tmp/vmware-install.bundle && \  
/tmp/vmware-install.bundle \--eulas-agreed \--console \--required && \  
rm /tmp/vmware-install.bundle && \  
apt-get -y clean  
  

