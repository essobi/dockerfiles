FROM debian:stable-slim  
  
RUN apt-get update && \  
apt-get install --no-install-recommends --yes iodine iptables && \  
rm -rf /var/lib/apt/lists/* && \  
mkdir -p /var/empty/iodined  
  
COPY entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh", "-f", "-t", "/var/empty/iodined", "-u",
"nobody"]  

