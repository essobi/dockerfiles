FROM lgpasquale/openvpn-client:latest  
  
RUN apt-get update && apt-get -y install iptables  
  
COPY redirect-and-init.sh /redirect-and-init.sh  
RUN chmod +x /redirect-and-init.sh  
  
ENTRYPOINT ["/redirect-and-init.sh"]  

