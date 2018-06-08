FROM debian:stretch-slim  
  
RUN \  
apt update && \  
apt install -y \  
curl \  
jq \  
netcat-openbsd && \  
apt-get clean autoclean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
ENV WAIT_SERVICE "service"  
ENV WAIT_PORT 80  
ENV WAIT_HOST WAITHOST  
ENV TIMEOUT 60  
ADD /entrypoint.sh /entrypoint.sh  
  
ENTRYPOINT ["/entrypoint.sh"]  

