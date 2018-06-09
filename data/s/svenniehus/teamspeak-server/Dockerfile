FROM ubuntu:15.10  
ENV TS3_VERSION 3.0.13.6  
ENV TS3_DIR /opt/ts3  
  
ADD scripts/start.sh /start.sh  
  
RUN apt-get update && apt-get -y install wget bzip2 screen  
  
# download TS3  
RUN wget -O /tmp/ts3-$TS3_VERSION.tar.gz
http://dl.4players.de/ts/releases/$TS3_VERSION/teamspeak3-server_linux_amd64-$TS3_VERSION.tar.bz2  
# extract to /opt  
RUN tar -xf /tmp/ts3-$TS3_VERSION.tar.gz -C /opt  
# move /opt/teamspeak-server_linux_amd64 to $TS3_DIR  
RUN mv /opt/teamspeak3-server_linux_amd64/ $TS3_DIR  
  
RUN mkdir -p /data/ts3/logs  
RUN mkdir -p /data/ts3/license  
RUN mkdir -p /data/ts3/cfg  
RUN touch /data/ts3/cfg/ip_blacklist.txt  
RUN touch /data/ts3/cfg/ip_whitelist.txt  
  
RUN adduser --disabled-password --gecos "" ts  
  
VOLUME ["/data/ts3"]  
CMD ["sh", "start.sh"]  
  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  

