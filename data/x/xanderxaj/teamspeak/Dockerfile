#
-----------------------------------------------------------------------------  
# docker-teamspeak  
#  
# Builds a basic Docker image that can run TeamSpeak  
# TeamSpeak: http://teamspeak.com  
# Docker: http://docker.com  
#
-----------------------------------------------------------------------------  
# Base system is the LTS version of Debian  
FROM debian:8  
# Set the Teamspeak version to download  
ENV tsv=3.0.13.8  
# Download and install everything from the repos.  
RUN DEBIAN_FRONTEND=noninteractive \  
apt-get -y update && \  
apt-get -y upgrade && \  
apt-get -y install bzip2 curl && \  
rm -fr /var/lib/apt/lists/*  
  
# Download and install TeamSpeak 3  
# Unzip with root permissions and move to correct location  
RUN curl
http://dl.4players.de/ts/releases/${tsv}/teamspeak3-server_linux_amd64-${tsv}.tar.bz2
| tar -xj --no-same-owner && \  
mv teamspeak3-server_linux_amd64 /opt/teamspeak  
  
# Add TeamSpeak user  
RUN useradd -s /usr/sbin/nologin teamspeak  
  
# Make volume directories so permissions can be set  
RUN mkdir -p /data/logs  
RUN chown -R teamspeak:teamspeak /data  
  
EXPOSE 9987/udp  
EXPOSE 30033  
EXPOSE 10011  
VOLUME ["/data"]  
USER teamspeak  
WORKDIR /data  
ENV LD_LIBRARY_PATH="/opt/teamspeak:${LD_LIBRARY_PATH}"  
CMD ["/opt/teamspeak/ts3server", "logpath=/data/logs",
"dbsqlpath=/opt/teamspeak/sql/"]  

