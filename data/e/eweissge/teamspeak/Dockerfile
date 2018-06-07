#FROM alpine:latest  
FROM frolvlad/alpine-glibc  
  
LABEL MAINTAINTER : Eric Weissgerber  
  
ENV TEAMSPEAK_VERSION 3.0.13.6  
RUN mkdir /opt \  
&& wget
http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_amd64-${TEAMSPEAK_VERSION}.tar.bz2
-O /tmp/teamspeak.tar.bz2 \  
&& tar jxf /tmp/teamspeak.tar.bz2 -C /opt \  
&& mv /opt/teamspeak3-server_* /opt/teamspeak \  
&& rm /tmp/teamspeak.tar.bz2\  
&& addgroup -g 503 teamspeak \  
&& adduser -u 503 -G teamspeak -h /opt/teamspeak -S -D teamspeak \  
&& chown -R teamspeak:teamspeak /opt/teamspeak  
  
VOLUME ["/opt/teamspeak"]  
VOLUME ["/data"]  
EXPOSE 9987/udp 10011 30033  
USER teamspeak  
ENTRYPOINT ["/data/teamspeak/ts3server_minimal_runscript.sh"]  
#ENTRYPOINT ["/bin/sh"]  

