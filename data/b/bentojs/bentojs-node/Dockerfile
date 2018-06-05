FROM debian:jessie  
  
RUN apt-get update && apt-get install -y --no-install-recommends \  
ca-certificates \  
curl \  
build-essential \  
pkg-config \  
lsof wget unzip gawk git \  
&& rm -rf /var/lib/apt/lists/*  
  
ENV NODE_VERSION "6.0.0"  
RUN curl
https://nodejs.org/dist/v${NODE_VERSION}/node-v${NODE_VERSION}-linux-x64.tar.gz
\  
|tar -xz -C /usr --strip-components=1  
  
CMD [ "node" ]  

