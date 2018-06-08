FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y \  
pound \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

