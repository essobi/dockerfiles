FROM parrotsec/parrot:latest  
MAINTAINER suntzu (suntzu@theartofwar.org)  
ENV DEBIAN_FRONTEND noninteractive  
  
# Install components  
RUN apt-get update && \  
apt-get -y dist-upgrade && \  
apt-get -y install parrot-pico \  
metasploit-framework \  
postgresql \  
parrot-mini \  
parrot-tools-cloud \  
parrot-menu \  
ipcalc \  
man && \  
apt-get -y autoremove  
  
ENTRYPOINT bash $@  

