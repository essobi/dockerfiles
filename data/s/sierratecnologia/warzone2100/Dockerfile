FROM ubuntu:xenial  
  
RUN apt-get update -y && \  
apt-get install -y warzone2100  
CMD /usr/local/bin/netbeans && \  
apt-get autoremove -y && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* && \  
rm -rf /tmp/*  
  
CMD /usr/games/warzone2100  

