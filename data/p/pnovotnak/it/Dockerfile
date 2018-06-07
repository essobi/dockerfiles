FROM ubuntu:xenial  
  
ENV DEBIAN_FRONTEND noninteractive  
ENV PATH "$PATH:/usr/share/bcc/tools/"  
  
RUN apt-get update -qy \  
&& apt-get install -qy \  
git \  
apt-transport-https \  
nmap \  
curl \  
wget \  
traceroute \  
inetutils-ping \  
mtr \  
strace \  
iotop \  
iftop \  
nethogs \  
htop \  
sudo \  
vim \  
dnsutils \  
net-tools \  
&& echo "deb [trusted=yes] https://repo.iovisor.org/apt/xenial xenial-nightly
main" \  
| tee /etc/apt/sources.list.d/iovisor.list \  
&& apt-get update -qy \  
&& apt-get install -qy \  
bcc-tools \  
&& rm -rf /var/lib/apt/lists/*  
  
VOLUME [ "/lib/modules" ]  
  

