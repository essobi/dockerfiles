FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install default-jre-headless \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

