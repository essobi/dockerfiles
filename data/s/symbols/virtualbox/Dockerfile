FROM debian:9  
  
LABEL maintainer="simon@widgit.com"  
  
RUN apt-get -y update && \  
echo "deb http://download.virtualbox.org/virtualbox/debian stretch contrib" >
/etc/apt/sources.list.d/virtualbox.list && \  
apt-get -y install linux-headers-amd64 wget gnupg procps openssh-client ca-
certificates && \  
wget -O /root/oracle_vbox_2016.asc
https://www.virtualbox.org/download/oracle_vbox_2016.asc && \  
apt-key add /root/oracle_vbox_2016.asc && \  
apt-get -y update && \  
apt-get -y install virtualbox-5.2 && \  
apt-get -y clean  
  

