FROM ubuntu:xenial  
MAINTAINER Alex McLain <alex@alexmclain.com>  
  
# Install system packages.  
RUN apt-get -qq update && \  
apt-get -y install wget bzip2 && \  
rm -rf /var/lib/apt/lists/*  
  
# Install TeamSpeak server.  
ENV TS_VERSION=3.0.13.6  
ENV
TS_DOWNLOAD_SHA256=19ccd8db5427758d972a864b70d4a1263ebb9628fcc42c3de75ba87de105d179  
  
RUN wget
http://dl.4players.de/ts/releases/${TS_VERSION}/teamspeak3-server_linux_amd64-${TS_VERSION}.tar.bz2
&& \  
echo "${TS_DOWNLOAD_SHA256}
teamspeak3-server_linux_amd64-${TS_VERSION}.tar.bz2" |sha256sum -c - && \  
tar -xjf teamspeak3-server_linux_amd64-${TS_VERSION}.tar.bz2 && \  
rm teamspeak3-server_linux_amd64-${TS_VERSION}.tar.bz2 && \  
mv teamspeak3-server_linux_amd64 /opt  
  
EXPOSE 9987/udp 10011 30033  
ENTRYPOINT
["/opt/teamspeak3-server_linux_amd64/ts3server_minimal_runscript.sh"]  

