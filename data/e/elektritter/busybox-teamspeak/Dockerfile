#
-----------------------------------------------------------------------------  
# docker-busybox-teamspeak  
#  
# Builds a basic docker image that can run TeamSpeak based on busybox  
# (http://teamspeak.com/).  
#  
# Original Authors: Isaac Bythewood  
# Authors: Rajko Albrecht  
# Updated: Sep 11, 2015  
# Require: Docker (http://www.docker.io/)  
#
-----------------------------------------------------------------------------  
FROM progrium/busybox  
  
# need curl && wget  
RUN opkg-install curl wget  
  
# Download and install TeamSpeak 3  
ADD ./scripts/setup_ts.sh /setup_ts.sh  
ADD ./scripts/backup_data.sh /backup_data.sh  
ADD ./scripts/restore_data.sh /restore_data.sh  
# /start runs it.  
ADD ./scripts/start.sh /start.sh  
ENV TS_VERSION=3.0.12.1  
RUN sh /setup_ts.sh &&\  
chown -R default /opt/teamspeak &&\  
mkdir /data &&\  
chown default:default /data &&\  
chmod +x /backup_data.sh&&\  
chmod +x /restore_data.sh &&\  
chmod +x /start.sh  
  
EXPOSE 9987/udp 10011 30033  
USER default  
VOLUME ["/data"]  
WORKDIR /data  
ENTRYPOINT ["/start.sh"]  
  

