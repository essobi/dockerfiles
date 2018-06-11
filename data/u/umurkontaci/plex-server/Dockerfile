FROM ubuntu:14.04  
RUN apt-get update -qq  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get -qq -y install curl  
  
ADD https://plex.tv/downloads/latest/1?channel=8&build=linux-
ubuntu-x86_64&distro=ubuntu&X-Plex-Token= /var/plex.deb  
  
RUN DEBIAN_FRONTEND=noninteractive dpkg -i /var/plex.deb 2>/dev/null || true  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -f -qq -y  
  
RUN DEBIAN_FRONTEND=noninteractive apt-get install -qq -y simpleproxy  
  
COPY start.sh /start.sh  
  
EXPOSE 32400 50000  
CMD ["/bin/sh", "start.sh"]  
  

