FROM node:8  
ARG DEBIAN_FRONTEND="noninteractive"  
# Install Bastion & its deps  
RUN \  
apt-get update && \  
apt-get install -y apt-utils && \  
apt-get dist-upgrade -y && \  
apt-get install -y build-essential git openssl python && \  
cd /opt && \  
git clone -b master -q --depth 1 https://github.com/TheBastionBot/Bastion.git
&& \  
cd Bastion && \  
npm install ffmpeg-binaries && \  
npm install  
  
# Volumes  
VOLUME /opt/Bastion/data /opt/Bastion/settings  
  
# Init  
WORKDIR /opt/Bastion  
ENTRYPOINT [ "node","." ]

