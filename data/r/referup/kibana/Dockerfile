FROM kibana:4.6.2  
RUN \  
apt-get update && \  
DEBIAN_FRONTEND=noninteractive \  
apt-get -y install \  
netcat \  
&& \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/*  
  
COPY entrypoint.sh /tmp/entrypoint.sh  
RUN chmod +x /tmp/entrypoint.sh  
  
CMD ["/tmp/entrypoint.sh"]  

