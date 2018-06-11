FROM ubuntu:16.04  
MAINTAINER Diego Tiscornia <diegobt@gmail.com>  
  
ENV HOME /root  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && apt-get install -y wget apt-utils  
  
RUN echo "deb http://download.virtualbox.org/virtualbox/debian xenial contrib"
| tee -a /etc/apt/sources.list  
  
RUN wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- |
apt-key add -  
RUN wget -q https://www.virtualbox.org/download/oracle_vbox.asc -O- | apt-key
add -  
  
RUN apt-get update && apt-get install virtualbox-5.0 -y  
  
# Install Virtualbox Extension Pack  
RUN VBOX_VERSION=`dpkg -s virtualbox-5.0 | grep '^Version: ' | sed -e
's/Version: \\([0-9\\.]*\\)\\-.*/\1/'` ; \  
wget
http://download.virtualbox.org/virtualbox/${VBOX_VERSION}/Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VERSION}.vbox-
extpack ; \  
VBoxManage extpack install
Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VERSION}.vbox-extpack ; \  
rm Oracle_VM_VirtualBox_Extension_Pack-${VBOX_VERSION}.vbox-extpack  
  
RUN apt-get clean && rm -rf /var/lib/apt/lists/*  
  
ENV QT_X11_NO_MITSHM=1  
ENV DISPLAY :0  
VOLUME /dev/vboxdrv  

