FROM debian:jessie  
  
RUN \  
apt-get update && \  
apt-get install -y --no-install-recommends \  
dnsutils \  
&& \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT [ "dig" ]

