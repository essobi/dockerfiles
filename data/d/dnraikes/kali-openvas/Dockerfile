#############################################  
# File: kali-openvas/Dockerfile  
# Author: Donald Raikes <don.raikes@oracle.com>  
# Date: 12/13/2016  
#  
# 01/19/2017 draikes changed to pull from kalilinux/kali-linux-docker image  
#############################################  
FROM kalilinux/kali-linux-docker  
MAINTAINER Donald Raikes  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y aptitude metasploit-framework rpcbind nfs-common
wireshark nmap \  
openvas rpm nsis alien  
  
RUN service postgresql start  
RUN /usr/bin/msfdb init  
  
RUN mkdir /root/bin  
COPY bin/* /root/bin/  
RUN chmod 777 /root/bin/*  
  
RUN echo "export PATH=.:$HOME/bin:$HOME:$PATH" >> /root/.bashrc  
RUN echo "export TERM=cygwin" >> /root/.bashrc  
RUN echo "set ai ic ts=4" > /root/.exrc  
expost 80/TCP 443/TCP 9390/TCP 9391/TCP 9392/TCP  
VOLUME {"/public,/var/lib/postgresql,/root"}  
ENTRYPOINT service postgresql start && /bin/bash  

