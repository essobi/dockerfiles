FROM ubuntu:16.04  
RUN apt-get update && \  
apt-get install -y --no-install-recommends \  
dpkg-dev && \  
rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /  
  
VOLUME [ "/repo" ]  
  
WORKDIR /repo  
  
ENTRYPOINT ["/docker-entrypoint.sh"]  

