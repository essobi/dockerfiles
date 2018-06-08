FROM pataquets/ubuntu:trusty  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -y postfix \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

