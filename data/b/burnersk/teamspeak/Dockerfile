FROM debian:latest  
MAINTAINER burnersk <dockerhub@failmail.de>  
LABEL Description="Docker container for TeamSpeak. TeamSpeak allows computer
users to speak with fellow computer users." Vendor="burnersk"
Version="3.0.12.4"  
  
ENV TEAMSPEAK_VERSION="3.0.12.4"  
WORKDIR /  
  
RUN apt-get update \  
&& apt-get install -qy wget tar bzip2 \  
&& rm -rf /var/cache/apt/* \  
&& adduser --home /app --shell /usr/sbin/nologin --no-create-home --gecos
"TeamSpeak User,,," \--disabled-password --disabled-login teamspeak \  
&& wget -q -O /teamspeak3-server.tar.bz2
http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_amd64-${TEAMSPEAK_VERSION}.tar.bz2
\  
&& tar xjf /teamspeak3-server.tar.bz2 \  
&& mv /teamspeak3-server_linux_amd64 /app \  
&& mkdir -p /app/config /app/data /app/logs /app/files \  
&& ln -s /app/data/ts3server.sqlitedb /app/ts3server.sqlitedb  
  
COPY app/config/* /app/config/  
COPY app/bin/* /usr/local/bin/  
  
RUN chown -R teamspeak:teamspeak /app \  
&& chmod -R g-w,o= /app \  
&& chown teamspeak:teamspeak /usr/local/bin/teamspeak \  
&& chmod 0755 /usr/local/bin/teamspeak  
  
VOLUME /app/config  
VOLUME /app/data  
VOLUME /app/logs  
VOLUME /app/files  
  
EXPOSE 9987/udp  
EXPOSE 30033/tcp  
EXPOSE 10011/tcp  
#EXPOSE 41144/tcp  
WORKDIR /app  
USER teamspeak  
  
ENTRYPOINT ["teamspeak"]  
CMD ["inifile=/app/config/ts3server.ini"]  

