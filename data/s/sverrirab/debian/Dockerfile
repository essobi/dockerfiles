FROM debian:8  
  
RUN apt-get update && \  
apt-get install -y --force-yes \--no-install-recommends \  
apt-transport-https \  
ca-certificates \  
apt-utils \  
locales \  
locales-all  
  
# Safest choice while still supporting i18n.  
RUN localedef -i en_US -f UTF-8 en_US.UTF-8  
ENV LC_ALL en_US.UTF-8  
  
RUN apt-get install -y --force-yes \--no-install-recommends \  
sudo \  
curl \  
wget \  
zip \  
unzip \  
vim \  
traceroute \  
dnsutils \  
htop \  
netcat \  
telnet \  
openssh-client \  
python-pip  

