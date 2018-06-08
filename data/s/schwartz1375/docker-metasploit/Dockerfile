FROM kalilinux/kali-linux-docker  
  
MAINTAINER Matthew Schwartz "@schwartz1375"  
  
WORKDIR /root  
USER root  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && apt-get -y \  
dist-upgrade && apt-get clean && apt-get install -y\  
nmap vim tmux\  
metasploit-framework  
  
# Configure for locale for tmux to work  
RUN localedef -f UTF-8 -i en_US en_US.UTF-8  
  
VOLUME /root/.msf4  
VOLUME /tmp/data  
  
CMD ["/bin/bash"]  

