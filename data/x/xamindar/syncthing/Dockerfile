# Dockerfile for syncthing  
FROM xamindar/archlinux-base:2015-05-13  
MAINTAINER xamindar <junkxamindar@gmail.com>  
  
# Environment variables  
ENV HOME /syncfolders  
ENV SYNCTHING_CONFIG /config  
ENV SYNCTHING_USER nobody  
ENV SYNCTHING_ENABLED yes  
ENV DISCOVERY_SVR_ENABLED no  
ENV RELAY_SVR_ENABLED no  
ENV RELAY_POOL https://relays.syncthing.net/endpoint  
ENV RELAY_GLOBAL_RATE 125000000  
ENV RELAY_SESSION_RATE 125000000  
ENV RELAY_MESSAGE_TIMEOUT 1m0s  
ENV RELAY_NETWORK_TIMEOUT 2m0s  
ENV RELAY_PING_INTERVAL 1m0s  
#ENV RELAY_EXT_ADDRESS :22067  
# Copy additional files to container  
# install.sh script  
COPY install.sh /tmp/  
# Custom supervisord.conf file for docker container  
COPY supervisord.conf /etc/  
# preparation script for services.  
COPY prep-service.sh /home/  
COPY prep-service.conf /etc/supervisor.d/  
# syncthing program launch file for supervisor  
COPY syncthing.conf /etc/supervisor.d/  
# discoversrv program launch file for supervisor  
COPY discosrv.sh /home/  
COPY discosrv.conf /etc/supervisor.d/  
# relaysrv program launch file for supervisor  
COPY relaysrv.sh /home/  
COPY relaysrv.conf /etc/supervisor.d/  
# Run Install script  
RUN chmod +x /home/*  
RUN chmod +x /tmp/install.sh && /bin/bash /tmp/install.sh && rm
/tmp/install.sh  
  
# Volumes  
# Map /config to host defined config path (/mnt/user/appdata/syncthing)  
VOLUME /config  
# Map /syncfolders to host sync folder location (/mnt/user/syncthing) add more
as needed  
VOLUME /syncfolders  
# Ports in use by this application.  
EXPOSE 8384/tcp 22000/tcp 21027/udp 8443/tcp 22067 22070  
# run supervisord  
CMD ["supervisord", "-c", "/etc/supervisord.conf", "-n"]  

