# Dockerfile for TeamSpeak server on alpine linux  
# Author: Franklyn Alexander van der Toorn  
# Base system: Alpine with glibc support  
FROM frolvlad/alpine-glibc  
  
# Set the Teamspeak version to download  
ENV version=3.0.12.4  
# Download and install TeamSpeak  
ADD
http://dl.4players.de/ts/releases/${version}/teamspeak3-server_linux_amd64-${version}.tar.bz2
./  
RUN tar xjf teamspeak3-server_linux_amd64-$version.tar.bz2 && \  
mkdir /opt && \  
mv teamspeak3-server_linux_amd64 /opt/teamspeak && \  
rm teamspeak3-server_linux_amd64-$version.tar.bz2  
  
#Expose ports for TeamSpeak  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
# Create user, group and directories  
RUN addgroup teamspeak && \  
adduser -G teamspeak -Ss /usr/sbin/nologin teamspeak && \  
mkdir -p /data/logs && \  
mkdir -p /data/sql && \  
chown -R teamspeak:teamspeak /data  
  
# Define some more stuff  
VOLUME ["/data"]  
USER teamspeak  
WORKDIR /data  
ENV LD_LIBRARY_PATH="/opt/teamspeak:${LD_LIBRARY_PATH}"  
CMD ["/opt/teamspeak/ts3server", "logpath=/data/logs",
"dbsqlpath=/opt/teamspeak/sql/"]  

