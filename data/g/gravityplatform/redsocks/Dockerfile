FROM debian:jessie  
  
ENV DEBIAN_FRONTEND noninteractive  
  
ADD src /  
  
RUN apt-get update && \  
apt-get install -y redsocks iptables --no-install-recommends && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
ENTRYPOINT ["/usr/local/bin/redsocks.sh"]  

