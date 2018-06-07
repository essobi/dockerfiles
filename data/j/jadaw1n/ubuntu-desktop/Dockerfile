FROM ubuntu:15.10  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y \  
build-essential \  
software-properties-common \  
curl \  
unzip \  
vim \  
wget \  
lxde-core \  
lxterminal \  
tightvncserver \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV USER root  
ENV HOME /root  
  
WORKDIR /root  
  
EXPOSE 5901  
CMD bash -c 'vncserver :1 -geometry 1280x800 -depth 24 && tail -F
/root/.vnc/*.log'  
  

