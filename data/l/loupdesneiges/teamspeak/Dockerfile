FROM alpine:3.7  
MAINTAINER Loup-des-Neiges <contact@loup-des-neiges.com>  
  
RUN apk add --no-cache ca-certificates libstdc++ su-exec  
  
RUN set -eux; \  
addgroup -g 9987 ts3server; \  
adduser -u 9987 -Hh /var/ts3server -G ts3server -s /sbin/nologin -D ts3server;
\  
mkdir -p /var/ts3server /var/run/ts3server; \  
chown ts3server:ts3server /var/ts3server /var/run/ts3server; \  
chmod 777 /var/ts3server /var/run/ts3server  
  
ENV PATH "${PATH}:/opt/ts3server"  
RUN set -eux; \  
apk add --no-cache --virtual .fetch-deps tar w3m; \  
TEAMSPEAK_VER="$(w3m -dump https://www.teamspeak.com/downloads | grep -m 1
'Server 64-bit ' | awk '{print $NF}')"; \  
wget
http://dl.4players.de/ts/releases/${TEAMSPEAK_VER}/teamspeak3-server_linux_alpine-${TEAMSPEAK_VER}.tar.bz2
-O server.tar.bz2; \  
mkdir -p /opt/ts3server; \  
tar -xf server.tar.bz2 --strip-components=1 -C /opt/ts3server; \  
rm server.tar.bz2; \  
apk del .fetch-deps; \  
rm -rf /opt/ts3server/doc/; \  
rm -rf /opt/ts3server/serverquerydocs/; \  
rm -rf /opt/ts3server/tsdns/; \  
rm /opt/ts3server/CHANGELOG; \  
rm /opt/ts3server/LICENSE; \  
mv /opt/ts3server/*.so /opt/ts3server/redist/* /usr/local/lib; \  
ldconfig /usr/local/lib; \  
chown -R ts3server:ts3server /opt/ts3server  
  
VOLUME /var/ts3server/  
WORKDIR /var/ts3server/  
  
EXPOSE 9987/udp 10011 30033  
COPY entrypoint.sh /opt/ts3server  
ENTRYPOINT [ "entrypoint.sh" ]  
CMD [ "ts3server" ]  

