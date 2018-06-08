FROM nearpod/alpine-jvm:3.7-jdk8  
  
ARG KAFKA_VERSION=1.0.0  
ARG KAFKA_DIST=kafka_2.12-${KAFKA_VERSION}  
ARG KAFKA_USER=kafka  
ARG KAFKA_HOME=/usr/local/$KAFKA_DIST  
ARG KAFKA_DATA_DIR=/var/lib/kafka/data  
ARG KAFKA_DATA_LOG_DIR=/var/lib/kafka/log  
ARG KAFKA_LOG_DIR=/var/log/kafka  
  
ENV KAFKA_USER=$KAFKA_USER \  
KAFKA_DATA_DIR=$KAFKA_DATA_DIR \  
KAFKA_HOME=$KAFKA_HOME  
ENV PATH=$PATH:$KAFKA_HOME/bin  
  
RUN set -ex; \  
WORKDIR="$PWD"; \  
apk --no-cache add gnupg; \  
curl -q -sSLO
"http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_DIST.tgz"; \  
curl -q -sSLO
"http://www.apache.org/dist/kafka/$KAFKA_VERSION/$KAFKA_DIST.tgz.asc"; \  
curl -q -sSLO "http://kafka.apache.org/KEYS"; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --import KEYS; \  
gpg --batch --verify "$KAFKA_DIST.tgz.asc" "$KAFKA_DIST.tgz"; \  
mkdir -p "$KAFKA_HOME"; \  
tar -xzf "$KAFKA_DIST.tgz" \--strip-components=1 -C "$KAFKA_HOME"; \  
rm -rf "$GNUPGHOME" KEYS "$KAFKA_DIST.tgz" "$KAFKA_DIST.tgz.asc"; \  
apk del gnupg  
  
COPY log4j.properties $KAFKA_HOME/config/  
  
RUN set -ex; \  
WORKDIR="$PWD"; \  
mkdir -p "$KAFKA_DATA_DIR"; \  
addgroup -g 1000 "$KAFKA_USER"; \  
adduser -D -h "$KAFKA_DATA_DIR" -u 1000 -G "$KAFKA_USER" "$KAFKA_USER"; \  
[ `id -u "$KAFKA_USER"` -eq 1000 ]; \  
[ `id -g "$KAFKA_USER"` -eq 1000 ]; \  
chown -R "$KAFKA_USER:$KAFKA_USER" "$KAFKA_HOME"; \  
chown -R "$KAFKA_USER:$KAFKA_USER" "$KAFKA_DATA_DIR"  
  
USER kafka:kafka  

