FROM ubuntu:xenial  
  
RUN apt-get update && apt-get install -y openconnect iptables  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
ADD iptables.sh /iptables.sh  
RUN chmod +x /iptables.sh  
ENTRYPOINT ["/iptables.sh"]  
CMD ["/start.sh"]

