FROM debian:stretch-slim  
  
MAINTAINER wilkesystems <maintainer@wilke.systems>  
  
ENV TINI_VERSION v0.13.1  
  
ADD https://github.com/krallin/tini/releases/download/${TINI_VERSION}/tini
/usr/bin/tini  
  
RUN apt-get update && apt-get install -y bzip2 curl w3m; rm -rf
/var/lib/apt/lists/*; chmod +x /usr/bin/tini; \  
groupadd -g 999 teamspeak; useradd -u 999 -g 999 -d /opt/teamspeak teamspeak;
mkdir -p /data /opt/teamspeak; \  
TEAMSPEAK_VERSION="$(w3m -dump https://www.teamspeak.com/downloads | grep -m 1
'Server 64-bit ' | awk '{print $NF}')"; \  
curl -sSL
http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_amd64-${TEAMSPEAK_VERSION}.tar.bz2
| \  
tar xj --strip-components=1 \--directory /opt/teamspeak --no-same-owner; \  
chown -R teamspeak:teamspeak /opt/teamspeak /data; \  
apt-get purge -y bzip2 curl w3m; apt-get autoremove -y; \  
rm -rf /var/lib/apt/lists/*  
  
COPY docker-entrypoint.sh /usr/bin/docker-entrypoint.sh  
  
WORKDIR /opt/teamspeak  
  
USER teamspeak  
  
EXPOSE 9987/udp 10011/tcp 30033/tcp 41144/tcp  
  
ENTRYPOINT ["docker-entrypoint.sh"]

