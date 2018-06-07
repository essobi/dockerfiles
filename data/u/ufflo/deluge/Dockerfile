FROM ubuntu:trusty  
MAINTAINER Olof Nilsson <olof@drp.nu>  
  
# Workaround to get rid of ugly red text when building from Dockerfile  
ENV DEBIAN_FRONTEND "noninteractive"  
# Install Deluge and WebGUI  
RUN apt-get install -qy software-properties-common && \  
add-apt-repository ppa:deluge-team/ppa && \  
apt-get update -q && \  
apt-get install -qy \  
deluged \  
deluge-web && \  
rm -rf /var/lib/apt/lists/*  
  
# Inject Startup Script  
ADD start.sh /start.sh  
RUN chmod +x /start.sh  
  
# Expose Volumes  
VOLUME ["/config", \  
"/log", \  
"/data"]  
  
# Expose Port - WebGUI  
EXPOSE 8112  
# Expose Port - Daemon  
EXPOSE 58846  
# Expose Ports - Torrent traffic  
EXPOSE 58847  
EXPOSE 58847/udp  
  
# Call Startup Script  
CMD ["/start.sh"]  

