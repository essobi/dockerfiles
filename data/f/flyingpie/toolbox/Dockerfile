FROM ubuntu:16.04  
MAINTAINER Marco van den Oever <marco@flyingpie.nl>  
  
RUN DEBIAN_FRONTEND=noninteractive  
  
# Prerequisites  
RUN apt-get update && apt-get install -y \  
apt-transport-https \  
ca-certificates \  
curl \  
software-properties-common  
  
RUN add-apt-repository "deb [arch=amd64]
https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable"  
RUN curl -fsSL https://download.docker.com/linux/ubuntu/gpg | apt-key add -  
  
# Apps  
RUN apt-get update && apt-get install -y \  
docker-ce \  
fish \  
libcurl3 \  
libicu55 \  
libunwind8 \  
toilet toilet-fonts \  
vim \  
wget  
  
# Powershell  
RUN wget -q $(curl -s
https://api.github.com/repos/powershell/powershell/releases/latest | grep
'browser_' | grep 'ubuntu1.16' | cut -d\" -f4)  
RUN dpkg -i $(ls / | grep powershell)  
  
# Config  
ADD image/root /root  
  
# Scripts  
RUN chmod +x /root/bin/*  
  
# Startup  
ADD image/toolbox.sh /toolbox.sh  
RUN chmod +x /toolbox.sh  
  
RUN echo "Build: $(date) @ $HOSTNAME" >> /build-info.txt  
  
WORKDIR "/root"  
ENTRYPOINT ["/toolbox.sh"]  

