FROM ubuntu:14.04  
RUN apt-get update -qq  
  
ADD http://download-
new.utorrent.com/endpoint/utserver/os/linux-x64-debian-7-0/track/beta/
/tmp/utserver.tar.gz  
  
WORKDIR /tmp  
RUN tar -xzvf utserver.tar.gz  
RUN rm utserver.tar.gz  
  
WORKDIR /tmp/utorrent-server-alpha-v3_3  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install libssl0.9.8 curl
unzip  
  
ADD utserver.conf /etc/utserver.conf  
  
RUN mkdir -p /opt/utserver/  
  
EXPOSE 6681  
EXPOSE 8080  
ADD start.sh /opt/start.sh  
ADD update-plex.sh /opt/update-plex.sh  
RUN chmod +x /opt/update-plex.sh  
CMD ["/bin/sh", "/opt/start.sh"]  

