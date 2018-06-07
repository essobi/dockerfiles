FROM debian:stable-slim  
  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get install -yq --no-install-recommends iproute2 iputils-ping fping
traceroute netcat nmap curl && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists  
  
CMD /bin/bash  

