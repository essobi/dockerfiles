FROM ubuntu-debootstrap:14.04  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
wget \  
apt-transport-https \  
&& rm -rf /var/lib/apt/lists/*;  

