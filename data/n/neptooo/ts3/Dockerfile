###############################################  
# Ubuntu with added Teamspeak 3 Server.  
# Uses SQLite Database on default.  
###############################################  
  
# Using 14.04 Ubuntu image as base.  
FROM ubuntu:14.04  
MAINTAINER Jean-Michel LE <jeanmile.le@gmail.com>  
  
## Set env variables.  
# Download lastest TS3 Server.  
ENV TEAMSPEAK_URL
http://dl.4players.de/ts/releases/3.0.11.3/teamspeak3-server_linux-
amd64-3.0.11.3.tar.gz  
  
# Inject a Volume for any TS3-Data that needs to be persisted or to be
accessible from the host. (e.g. for Backups)  
VOLUME ["/teamspeak3"]  
  
ADD run.sh /run.sh  
RUN chmod 774 /run.sh  
  
# Download TS3 file and extract it into /opt.  
ADD ${TEAMSPEAK_URL} /opt/  
RUN cd /opt && tar -xzf /opt/teamspeak3-server_linux-amd64-3*.tar.gz  
  
# Add teamspeak user  
RUN adduser --disabled-password --gecos "" teamspeak  
  
# Change permissions folder.  
RUN chown -R teamspeak:teamspeak /opt/teamspeak3-server_linux-amd64/  
RUN chown -R teamspeak:teamspeak /teamspeak3  
  
  
USER teamspeak  
  
ENTRYPOINT ["/run.sh"]  
  
# Expose the Standard TS3 port.  
EXPOSE 9987/udp  
# for files  
EXPOSE 30033  
# for ServerQuery  
EXPOSE 10011  

