FROM stakater/base-alpine:3.5  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
# https://artifacts.elastic.co/GPG-KEY-elasticsearch  
ENV GPG_KEY 46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV FILEBEAT_PATH /usr/share/filebeat  
ENV PATH $FILEBEAT_PATH:$PATH  
  
ARG FILEBEAT_VERSION=5.2.1  
ENV
FILEBEAT_TARBALL="https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-${FILEBEAT_VERSION}-linux-x86_64.tar.gz"
\  
FILEBEAT_TARBALL_ASC="https://artifacts.elastic.co/downloads/beats/filebeat/filebeat-5.2.1-linux-x86_64.tar.gz.asc"
\  
FILEBEAT_TARBALL_SHA1="694fe12e56ebf8e4c4b11b590cfb46c662e7a3c1"  
RUN set -ex; \  
\  
apk add \--no-cache --virtual .fetch-deps \  
ca-certificates \  
gnupg \  
openssl \  
tar \  
; \  
\  
wget -O filebeat.tar.gz "$FILEBEAT_TARBALL"; \  
\  
if [ "$FILEBEAT_TARBALL_SHA1" ]; then \  
echo "$FILEBEAT_TARBALL_SHA1 *filebeat.tar.gz" | sha1sum -c -; \  
fi; \  
\  
if [ "$FILEBEAT_TARBALL_ASC" ]; then \  
wget -O filebeat.tar.gz.asc "$FILEBEAT_TARBALL_ASC"; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY"; \  
gpg --batch --verify filebeat.tar.gz.asc filebeat.tar.gz; \  
rm -r "$GNUPGHOME" filebeat.tar.gz.asc; \  
fi; \  
\  
mkdir -p "$FILEBEAT_PATH"; \  
tar -xf filebeat.tar.gz \--strip-components=1 -C "$FILEBEAT_PATH"; \  
rm filebeat.tar.gz; \  
\  
apk del .fetch-deps; \  
\  
filebeat --version;  
  
ADD ./config/filebeat.yml /etc/filebeat/filebeat.yml  
  
# Simulate cmd behavior via environment variable  
# So that users are able to provice command line arguments to filbeat  
ENV COMMAND "filebeat -c /etc/filebeat/filebeat.yml"  
# Make daemon service dir for filebeat and place file  
# It will be started and maintained by the base image  
RUN mkdir -p /etc/service/filebeat  
ADD start.sh /etc/service/filebeat/run  
# Use base image's entrypoint

