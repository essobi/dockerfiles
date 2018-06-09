FROM ubuntu  
MAINTAINER Gabriel Gayan  
  
RUN apt-get update  
RUN apt-get install -y wget  
RUN cd /opt  
RUN cd /opt; wget
http://dl.4players.de/ts/releases/3.0.10.3/teamspeak3-server_linux-
amd64-3.0.10.3.tar.gz  
RUN cd /opt; tar xvzf teamspeak3-server_linux-amd64-3.0.10.3.tar.gz  
RUN cd /opt; rm teamspeak3-server_linux-amd64-3.0.10.3.tar.gz  
RUN cd /opt; mv teamspeak3-server_linux-amd64 teamspeak3-server  
  
EXPOSE 9987/udp  
  
CMD ["/opt/teamspeak3-server/ts3server_minimal_runscript.sh"]  

