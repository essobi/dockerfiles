# ----------------------------------  
# PixARK Warband Dockerfile  
# Environment: Ubuntu:16.04 + Wine  
# Minimum Panel Version: 0.7.6  
# ----------------------------------  
FROM ubuntu:16.04  
MAINTAINER Kenny B, <kenny@venatus.digital>  
  
# Install Dependencies  
RUN dpkg --add-architecture i386 && \  
apt update && \  
apt upgrade -y && \  
apt install -y wget software-properties-common apt-transport-https lib32gcc1
&& \  
wget https://dl.winehq.org/wine-builds/Release.key && \  
apt-key add Release.key && \  
apt-add-repository 'https://dl.winehq.org/wine-builds/ubuntu/' -y && \  
apt update && \  
apt install -y winehq-stable && \  
apt clean && \  
useradd -d /home/container -m container && \  
cd /home/container  
  
USER container  
ENV HOME /home/container  
WORKDIR /home/container  
  
COPY ./entrypoint.sh /entrypoint.sh  
CMD ["/bin/bash", "/entrypoint.sh"]  

