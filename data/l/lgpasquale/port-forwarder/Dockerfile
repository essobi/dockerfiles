FROM debian:stable  
  
RUN apt-get update && apt-get -y install iptables  
  
COPY init.sh /init.sh  
RUN chmod +x /init.sh  
  
ENTRYPOINT ["/init.sh"]  

