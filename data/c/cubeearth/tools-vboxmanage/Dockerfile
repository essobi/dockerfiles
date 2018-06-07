FROM ubuntu:16.04  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget -q https://www.virtualbox.org/download/oracle_vbox_2016.asc -O- | apt-key
add - && \  
sh -c 'echo "deb http://download.virtualbox.org/virtualbox/debian xenial
contrib" >> /etc/apt/sources.list.d/virtualbox.list' && \  
apt-get update && \  
apt-get install -y virtualbox-5.1  
  
#RUN /usr/bin/VBoxManage setextradata global GUI/SuppressMessages "all"  
COPY VBoxManageWrapper.sh /usr/bin  
  
Volume /data  
  
ENTRYPOINT [ "/usr/bin/VBoxManageWrapper.sh" ]  

