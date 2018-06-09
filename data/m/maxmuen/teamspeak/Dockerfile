FROM frolvlad/alpine-glibc:latest  
MAINTAINER github@maxmuen.de  
  
LABEL org.label-schema.schema-version="1.0" \  
org.label-schema.build-date="2017-08-30T23:19:19+02:00" \  
org.label-schema.name="Teamspeak" \  
org.label-schema.description="Voice chat software designed with security in
mind, featuring crystal clear voice quality, scalability up to thousands of
users, and endless customization options. Packed with powerful features and
incredible performance, TeamSpeak is your Swiss Army Knife of voice
communication." \  
org.label-schema.url="http://teamspeak.com" \  
org.label-schema.version="3.0.13.8" \  
org.label-schema.docker.cmd="docker run -d --name "teamspeak" -p
"9987:9987/udp" -p "10011:10011/tcp" -p "30033:30033/tcp" -v
"${PWD}/data:/data" teamspeak"  
  
RUN apk --update \--no-cache --virtual=.build-dependencies add curl \  
&& curl -sL
'http://teamspeak.gameserver.gamed.de/ts3/releases/3.0.13.8/teamspeak3-server_linux_amd64-3.0.13.8.tar.bz2'
| tar xvjkf - -C /tmp \  
&& mkdir /opt \  
&& mv /tmp/teamspeak3-server_linux_amd64 /opt/teamspeak \  
&& ln -s /data/files /opt/teamspeak/files \  
&& ln -s /data/ts3server.ini /opt/teamspeak/ts3server.ini \  
&& ln -s /data/ts3server.sqlitedb /opt/teamspeak/ts3server.sqlitedb \  
&& ln -s /data/licensekey.dat /opt/teamspeak/licensekey.dat \  
&& apk del .build-dependencies \  
&& apk --update \--no-cache add su-exec \  
&& adduser -u 50001 -h /opt/teamspeak -S -D teamspeak \  
&& chown teamspeak:root -R /opt/teamspeak \  
&& mkdir -p /opt/teamspeak/data-skeleton/files  
  
EXPOSE 9987/udp \  
10011/tcp \  
30033/tcp  
  
COPY scripts/entrypoint /usr/local/bin/entrypoint  
COPY data /opt/teamspeak/data-skeleton/  
  
VOLUME ["/data/"]  
  
WORKDIR "/opt/teamspeak"  
ENTRYPOINT ["entrypoint"]  

