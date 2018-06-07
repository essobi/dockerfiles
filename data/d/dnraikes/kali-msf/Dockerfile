#############################################  
# File: kali-msf/Dockerfile  
# Author: Donald Raikes <don.raikes@oracle.com>  
# Date: 12/13/2016  
#############################################  
FROM dnraikes/kali-base  
MAINTAINER Donald Raikes  
RUN apt-get update && apt-get -y upgrade  
RUN apt-get install -y aptitude metasploit-framework rpcbind nfs-common
wireshark nmap \  
nikto scapy  
  
RUN service postgresql start nmap  
RUN /usr/bin/msfdb init  
RUN nikto update  
  
VOLUME {"/public,/var/lib/postgresql,/root"}  
ENTRYPOINT service postgresql start && /bin/bash  

