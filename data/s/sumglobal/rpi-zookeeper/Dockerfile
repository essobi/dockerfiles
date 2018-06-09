FROM sumglobal/rpi-openjdk:8-jdk-azul  
  
LABEL maintainer="Charles Walker <cwalker@sumglobal.com>, Chip Dickson
<cdickson@sumglobal.com>"  
  
RUN [ "cross-build-start" ]  
  
# Install required packages  
RUN apt-get update \  
&& apt-get install -y curl python wget netcat-openbsd  
  
ENV ZOO_USER=zookeeper \  
ZOO_CONF_DIR=/conf \  
ZOO_DATA_DIR=/zk/data \  
ZOO_DATA_LOG_DIR=/zk/datalog \  
ZOO_PORT=2181 \  
ZOO_TICK_TIME=2000 \  
ZOO_INIT_LIMIT=5 \  
ZOO_SYNC_LIMIT=2  
# Add a user and make dirs  
RUN set -x \  
&& useradd "$ZOO_USER" \  
&& [ `id -u $ZOO_USER` -eq 1000 ] \  
&& [ `id -g $ZOO_USER` -eq 1000 ] \  
&& mkdir -p "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR" "$ZOO_CONF_DIR" \  
&& chown "$ZOO_USER:$ZOO_USER" "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR"
"$ZOO_CONF_DIR"  
  
ARG GPG_KEY=C823E3E5B12AF29C67F81976F5CECB3CB5E9BD2D  
ARG DISTRO_NAME=zookeeper-3.4.10  
# Download Apache Zookeeper, verify its PGP signature, untar and clean up  
RUN set -x \  
&& wget -q
"http://www.apache.org/dist/zookeeper/$DISTRO_NAME/$DISTRO_NAME.tar.gz" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& tar -xzf "$DISTRO_NAME.tar.gz" \  
&& mv "$DISTRO_NAME/conf/"* "$ZOO_CONF_DIR" \  
&& rm -r "$GNUPGHOME" "$DISTRO_NAME.tar.gz" \  
&& rm -rf $DISTRO_NAME/CHANGES.txt \  
$DISTRO_NAME/README.txt \  
$DISTRO_NAME/NOTICE.txt \  
$DISTRO_NAME/CHANGES.txt \  
$DISTRO_NAME/README_packaging.txt \  
$DISTRO_NAME/build.xml \  
$DISTRO_NAME/config \  
$DISTRO_NAME/contrib \  
$DISTRO_NAME/dist-maven \  
$DISTRO_NAME/docs \  
$DISTRO_NAME/ivy.xml \  
$DISTRO_NAME/ivysettings.xml \  
$DISTRO_NAME/recipes \  
$DISTRO_NAME/src \  
$DISTRO_NAME/$DISTRO_NAME.jar.asc \  
$DISTRO_NAME/$DISTRO_NAME.jar.md5 \  
$DISTRO_NAME/$DISTRO_NAME.jar.sha1 \  
&& apt-get autoremove -y wget \  
&& rm -rf /var/lib/apt/lists/*  
  
WORKDIR $DISTRO_NAME  
VOLUME ["$ZOO_DATA_DIR", "$ZOO_DATA_LOG_DIR"]  
  
EXPOSE $ZOO_PORT 2888 3888  
ENV PATH=$PATH:/$DISTRO_NAME/bin \  
ZOOCFGDIR=$ZOO_CONF_DIR  
# Tone down the JVM heap etc. for the RASPI we only have 1G  
ENV ZK_SERVER_HEAP 384  
ENV ZK_CLIENT_HEAP 128  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["zkServer.sh", "start-foreground"]  
  
RUN [ "cross-build-end" ]

