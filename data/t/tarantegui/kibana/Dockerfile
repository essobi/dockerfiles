FROM kibana  
  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
netcat \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY docker-init /docker-init  
RUN chmod +x /docker-init  
  
CMD ["/docker-init"]  

