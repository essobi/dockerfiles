FROM debian:stable-slim  
  
# Monero P2P  
EXPOSE 18080  
# Monero RPC  
EXPOSE 18081  
WORKDIR /monero  
  
RUN apt-get update -q && \  
apt-get install -y curl bzip2 && \  
useradd -m monero && \  
curl -L https://downloads.getmonero.org/linux64 | tar jx && \  
mv monero-v*/* . && rmdir monero-v* && \  
apt-get purge -y curl bzip2 && \  
apt-get autoremove --purge -y && \  
rm -rf /var/tmp/* /tmp/* /var/lib/apt/lists/*  
  
VOLUME /home/monero  
COPY entrypoint.sh /  
  
USER monero  
ENTRYPOINT ["/entrypoint.sh"]  

