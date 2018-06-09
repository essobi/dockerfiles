FROM pataquets/emailrelay  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
uuid \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  

