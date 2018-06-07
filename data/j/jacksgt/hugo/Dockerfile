FROM debian:stretch  
  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
hugo \  
python3-pygments \  
&& apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /opt/blog  
  
WORKDIR /opt/blog  
  
VOLUME /opt/blog  

