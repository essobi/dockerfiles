FROM debian:jessie  
MAINTAINER Vincent Rouille "vincent@speedy37.fr"  
ENV TS3_DIR /opt/teamspeak3-server  
RUN mkdir -p /opt \  
&& apt-get update && apt-get install -y curl bzip2 \  
&& curl
http://dl.4players.de/ts/releases/3.0.13.6/teamspeak3-server_linux_amd64-3.0.13.6.tar.bz2
| tar -xj \  
&& mv teamspeak3-server_linux_amd64 $TS3_DIR \  
&& ln -s /data/ts3server.sqlitedb $TS3_DIR/ts3server.sqlitedb \  
&& ln -s /data/files $TS3_DIR/files \  
&& ln -s /data/licensekey.dat $TS3_DIR/licensekey.dat  
  
VOLUME /data  
  
EXPOSE 9987/udp 10011 30033  
CMD ["/opt/teamspeak3-server/ts3server_minimal_runscript.sh"]  

