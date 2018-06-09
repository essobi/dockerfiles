FROM debian:stretch  
  
RUN set -ex && \  
apt-get update && \  
apt-get install -y --no-install-recommends stuntman-server && \  
apt-get clean -y && \  
rm -rf /var/lib/apt/lists/*  
  
EXPOSE 3478/tcp 3478/udp  
  
USER nobody  
  
ENTRYPOINT ["/usr/sbin/stunserver"]  
  

