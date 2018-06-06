FROM redis:3.2.4  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
dnsutils \  
netcat \  
&& \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  

