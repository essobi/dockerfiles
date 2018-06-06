FROM openjdk:8-jre-alpine  
  
LABEL name="Apache Zookeeper" \  
version="3.4.5" \  
maintainer="Christos Manios <maniopaido@gmail.com>"  
# Install required packages  
RUN apk add \--no-cache \  
bash \  
su-exec  
  
ENV ZOO_USER=zookeeper \  
ZOO_CONF_DIR=/conf \  
ZOO_DATA_DIR=/data \  
ZOO_DATA_LOG_DIR=/datalog \  
ZOO_PORT=2181 \  
ZOO_TICK_TIME=2000 \  
ZOO_INIT_LIMIT=5 \  
ZOO_SYNC_LIMIT=2 \  
ZOO_MAX_CLIENT_CNXNS=60  
  
# Add a user and make dirs  
RUN set -ex; \  
adduser -D "$ZOO_USER"; \  
mkdir -p "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR" "$ZOO_CONF_DIR"; \  
chown "$ZOO_USER:$ZOO_USER" "$ZOO_DATA_LOG_DIR" "$ZOO_DATA_DIR"
"$ZOO_CONF_DIR"  
  
ARG GPG_KEY=B6B3F7EDA5BA7D1E827DE5180DFF492D8EE2F25C  
ARG DISTRO_NAME=zookeeper-3.4.5  
  
# Download Apache Zookeeper, verify its PGP signature, untar and clean up  
RUN set -ex; \  
apk add \--no-cache --virtual .build-deps \  
gnupg; \  
wget -q
"http://archive.apache.org/dist/zookeeper/$DISTRO_NAME/$DISTRO_NAME.tar.gz"; \  
wget -q
"http://archive.apache.org/dist/zookeeper/$DISTRO_NAME/$DISTRO_NAME.tar.gz.asc";
\  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-key "$GPG_KEY" || \  
gpg --keyserver pgp.mit.edu --recv-keys "$GPG_KEY" || \  
gpg --keyserver pgpkeys.mit.edu --recv-keys "$GPG_KEY"; \  
gpg --batch --verify "$DISTRO_NAME.tar.gz.asc" "$DISTRO_NAME.tar.gz"; \  
tar -xzf "$DISTRO_NAME.tar.gz"; \  
mv "$DISTRO_NAME/conf/"* "$ZOO_CONF_DIR"; \  
rm -rf "$GNUPGHOME" "$DISTRO_NAME.tar.gz" "$DISTRO_NAME.tar.gz.asc"; \  
apk del .build-deps  
  
WORKDIR $DISTRO_NAME  
VOLUME ["$ZOO_DATA_DIR", "$ZOO_DATA_LOG_DIR"]  
  
EXPOSE $ZOO_PORT 2888 3888  
  
ENV PATH=$PATH:/$DISTRO_NAME/bin \  
ZOOCFGDIR=$ZOO_CONF_DIR  
  
COPY docker-entrypoint.sh /  
ENTRYPOINT ["/docker-entrypoint.sh"]  
CMD ["zkServer.sh", "start-foreground"]  

