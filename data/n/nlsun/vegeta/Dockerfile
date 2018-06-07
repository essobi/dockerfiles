FROM ubuntu:16.04  
  
RUN apt-get update && \  
apt-get install -y \  
curl \  
dnsutils \  
&& \  
mkdir /vegeta && \  
cd /vegeta && \  
curl -LO
https://github.com/tsenart/vegeta/releases/download/v6.1.1/vegeta-v6.1.1-linux-
amd64.tar.gz && \  
tar -xvf vegeta-* && \  
mv vegeta /bin/vegeta && \  
rm -rf /vegeta && \  
cd / && \  
apt-get autoclean -y && \  
apt-get autoremove -y && \  
rm -rf /var/lib/apt/lists/*  

