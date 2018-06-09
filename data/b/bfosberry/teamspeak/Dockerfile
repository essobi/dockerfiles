# Teamspeak 3 Server  
#  
# VERSION 0.1  
FROM bfosberry/gamekick_base  
MAINTAINER bfosberry  
  
# install teamspeak  
ENV TS3_VERSION 3.0.11.1  
ENV TS3_DIR /opt/teamspeak3-server  
RUN wget -O /tmp/teamspeak-server.tar.gz
http://dl.4players.de/ts/releases/$TS3_VERSION/teamspeak3-server_linux-
amd64-$TS3_VERSION.tar.gz  
RUN tar -xf /tmp/teamspeak-server.tar.gz -C /opt && mv
/opt/teamspeak3-server_linux-amd64 $TS3_DIR  
  
#RUN rm teamspeak3-server_linux-amd64-$TS3_VERSION.tar.gz  
# prep the data directory, this will get wiped when the volume is mounted  
# however this step ensures the links are set up correctly  
ENV PATH $TS3_DIR/scripts/:$PATH  
RUN mkdir -p $DATA_FOLDER/state  
  
WORKDIR $TS3_DIR  
  
VOLUME /opt/data  
  
# expose the teamspeak ports  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
# add the runner script  
ADD ./scripts /opt/teamspeak3-server/scripts  
ADD ./confd /opt/teamspeak3-server/confd  
  

