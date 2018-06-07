FROM ubuntu:14.04  
RUN \  
sed -i 's/# \\(.*multiverse$\\)/\1/g' /etc/apt/sources.list && \  
apt-get update && \  
apt-get -y upgrade && \  
apt-get install -y build-essential && \  
apt-get install -y curl git vim man htop  
  
ENV HOME /data  
  
WORKDIR /data  
  
CMD ['bash']  

