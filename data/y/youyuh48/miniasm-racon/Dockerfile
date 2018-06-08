# Docker container for minimap, miniasm, and racon  
# VERSION 0.1  
FROM ubuntu  
MAINTAINER youyuh48  
  
# Upgrade and install necessary packages:  
RUN apt-get update && apt-get upgrade -y &&\  
apt-get install -y \  
build-essential \  
git \  
zlib1g-dev &&\  
apt-get clean &&\  
rm -rf /var/lib/apt/lists/*  
  
# Start working in /opt  
WORKDIR /opt  
  
# Compile and install minimap:  
RUN git clone https://github.com/lh3/minimap && (cd minimap && make) &&\  
cp minimap/minimap /usr/local/bin && rm -r minimap  
  
# Compile and install miniasm:  
RUN git clone https://github.com/lh3/miniasm && (cd miniasm && make) &&\  
cp miniasm/miniasm /usr/local/bin/ && rm -r miniasm  
  
# Compile and install racon:  
RUN git clone https://github.com/isovic/racon.git &&\  
(cd racon && make modules && make tools && make) &&\  
cp racon/bin/racon /usr/local/bin/ && rm -r racon  

