FROM node:latest  
  
RUN apt-get update && \  
apt-get install -y wget && \  
wget -q https://dl.google.com/linux/direct/google-chrome-
stable_current_amd64.deb && \  
dpkg --unpack google-chrome-stable_current_amd64.deb && \  
apt-get install -f -y && \  
apt-get clean && \  
rm google-chrome-stable_current_amd64.deb  

