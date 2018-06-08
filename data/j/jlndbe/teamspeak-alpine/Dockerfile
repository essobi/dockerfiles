FROM frolvlad/alpine-glibc:latest  
  
ARG IMAGE_NAME  
ARG BUILD_DATE  
ARG VCS_REF  
  
ENV ARCH=amd64 \  
DOCKERIZE_VERSION=v0.6.0 \  
TEAMSPEAK_VERSION=3.0.13.8  
  
LABEL maintainer="Johlandabee <contact@jlndbe.me>" \  
description="A alpine based customizable TeamSpeak 3 server image without much
magic." \  
me.jlndbe.arch=${ARCH} \  
me.jlndbe.teamspeak-server-version=${TEAMSPEAK_VERSION} \  
me.jlndbe.dockerize-version=${DOCKERIZE_VERSION} \  
org.label-schema.schema-version="1.0.0-rc1" \  
org.label-schema.name=${IMAGE_NAME} \  
org.label-schema.build-date=${BUILD_DATE} \  
org.label-schema.vcs-url="https://github.com/Johlandabee/teamspeak-alpine.git"
\  
org.label-schema.vcs-ref=${VCS_REF}  
  
ENV PUID=1001 PGID=1001 \  
# Download sources  
DOCKERIZE_SOURCE="https://github.com/jwilder/dockerize/releases/download/${DOCKERIZE_VERSION}/dockerize-
alpine-linux-${ARCH}-${DOCKERIZE_VERSION}.tar.gz" \  
TEAMSPEAK_SOURCE="http://dl.4players.de/ts/releases/${TEAMSPEAK_VERSION}/teamspeak3-server_linux_${ARCH}-${TEAMSPEAK_VERSION}.tar.bz2"
\  
# Network  
TS_NET_IP_VOICE=0.0.0.0 \  
TS_NET_PORT_VOICE=9987 \  
TS_NET_IP_FILETRANSFER=0.0.0.0 \  
TS_NET_PORT_FILETRANFER=30033 \  
TS_NET_IP_SERVERQUERY=0.0.0.0 \  
TS_NET_PORT_SERVERQUERY=10011 \  
# Query white/blacklist  
TS_QUERY_IP_WHITELIST=query_ip_whitelist.txt \  
TS_QUERY_IP_BLACKLIST=query_ip_blacklist.txt \  
# Database  
TS_DB_CLEAR_DATABASE=0 \  
TS_DB_PLUGIN=ts3db_sqlite3 \  
TS_DB_PLUGIN_PARAMETER=ts3db_mariadb.ini \  
TS_DB_CONNECTIONS=10 \  
TS_DB_CLIENT_KEEP_DAYS=90 \  
TS_DB_LOG_KEEP_DAYS=90 \  
TS_DB_SQL_CREATE_PATH=create_sqlite/ \  
TS_DB_MARIADB_HOST=mariadb \  
TS_DB_MARIADB_PORT=3306 \  
TS_DB_MARIADB_USERNAME=teamspeak \  
TS_DB_MARIADB_PASSWORD= \  
TS_DB_MARIADB_DATABASE=teamspeak \  
TS_DB_MARIADB_SOCKET= \  
# Logs  
TS_LOG_PATH=logs/ \  
TS_LOG_APPEND=0 \  
TS_LOG_QUERY_COMMANDS=1 \  
# Misc  
TS_LICENSE_PATH=/app/config/licensekey.dat \  
TS_CREATE_DEFAULT_SERVER=1 \  
TS_MACHINE_ID=  
  
WORKDIR /app/  
COPY run.sh .  
RUN mkdir db/ config/ files/ logs/ \  
# Install curl  
&& apk update \  
&& apk add --virtual .image-setup curl tar \  
# Download Dockerize  
&& curl -L ${DOCKERIZE_SOURCE} | tar xzC /usr/local/bin \  
# Download Teamspeak binaries  
&& curl -L ${TEAMSPEAK_SOURCE} | tar -xjC . --strip 1 \  
# Create and link empty sqlite database file  
&& touch db/ts3server.sqlitedb \  
&& ln -s db/ts3server.sqlitedb ts3server.sqlitedb \  
# Prepare working directory  
&& mv redist/libmariadb.so.2 . \  
&& chmod +x run.sh \  
# Clean up  
&& apk del .image-setup \  
&& rm -rf /var/cache/apk/* \  
# Create user and set permissions  
&& addgroup -g ${PGID} app && adduser -D -u ${PUID} -G app app \  
&& chown -R app:app .  
  
VOLUME [ "/app/logs", "/app/files", "/app/db", "/app/config" ]  
  
EXPOSE ${TS_NET_PORT_VOICE}/udp \  
${TS_NET_PORT_FILETRANFER}/tcp \  
${TS_NET_PORT_SERVERQUERY}/tcp  
  
USER app  
ENTRYPOINT ["/app/run.sh"]

