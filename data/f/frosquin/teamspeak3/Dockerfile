FROM busybox:ubuntu-14.04  
MAINTAINER Frank Rosquin <frank.rosquin@gmail.com>  
  
ENV TS3_VERSION 3.0.11.1  
ENV DEBIAN_FRONTEND noninteractive  
  
RUN wget -O /tmp/teamspeak-server.tar.gz
http://dl.4players.de/ts/releases/$TS3_VERSION/teamspeak3-server_linux-
amd64-${TS3_VERSION}.tar.gz \  
&& gzip -d /tmp/teamspeak-server.tar.gz -c | tar -xf - -C /tmp \  
&& rm /tmp/teamspeak-server.tar.gz \  
&& mv /tmp/teamspeak3-server_linux-amd64 /teamspeak  
  
ADD ./ts3server /ts3server  
RUN chmod 755 /ts3server  
  
EXPOSE 9987/udp  
EXPOSE 10011  
EXPOSE 30033  
VOLUME ["/data"]  
  
ENTRYPOINT ["/ts3server"]  
CMD ["logpath=/data/logs/"]  

