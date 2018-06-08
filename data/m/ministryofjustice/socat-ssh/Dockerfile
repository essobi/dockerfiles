FROM debian:jessie  
  
RUN apt-get update && apt-get install -y socat && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && rm -fr *Release* *Sources* *Packages* && \  
truncate -s 0 /var/log/*log  
  
# You can override proxy port via ENV variable  
ENV SSH_AUTH_PROXY_PORT 1234  
COPY ./start /  
RUN chmod 700 /start  
  
CMD ["/start"]  

