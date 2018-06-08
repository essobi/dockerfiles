FROM debian:jessie  
  
RUN apt-get update && \  
apt-get upgrade -y && \  
apt-get install -y \  
sudo \  
pwgen \  
mumble-server && \  
apt-get clean && \  
rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*  
  
RUN useradd mumble  
  
ADD mumble-server.ini /etc/mumble-server.ini  
ADD run.sh /tmp/run.sh  
  
VOLUME ["/var/lib/mumble-server"]  
  
EXPOSE 64738/tcp 64738/udp  
  
CMD ["bash","/tmp/run.sh"]  

