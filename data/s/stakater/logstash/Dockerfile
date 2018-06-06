FROM stakater/java8-alpine:1.8.0_121  
LABEL authors="Hazim <hazim_malik@hotmail.com>"  
# grab su-exec for easy step-down from root  
# install plugin dependencies  
RUN apk add --no-cache 'su-exec>=0.2' libc6-compat libzmq  
  
# https://www.elastic.co/guide/en/logstash/5.0/installing-logstash.html#_apt  
# https://artifacts.elastic.co/GPG-KEY-elasticsearch  
ENV GPG_KEY 46095ACC8548582C1A2699A9D27D666CD88E42B4  
  
ENV LOGSTASH_PATH /usr/share/logstash/bin  
ENV PATH $LOGSTASH_PATH:$PATH  
  
ARG LOGSTASH_VERSION=5.2.1  
ENV
LOGSTASH_TARBALL="https://artifacts.elastic.co/downloads/logstash/logstash-5.2.1.tar.gz"
\  
LOGSTASH_TARBALL_ASC="https://artifacts.elastic.co/downloads/logstash/logstash-5.2.1.tar.gz.asc"
\  
LOGSTASH_TARBALL_SHA1="ba8c7fd6c3bb5455a5c86d7b4858d355cc7a26e8"  
  
RUN set -ex; \  
\  
if [ -z "$LOGSTASH_TARBALL_SHA1" ] && [ -z "$LOGSTASH_TARBALL_ASC" ]; then \  
echo >&2 'error: have neither a SHA1 _or_ a signature file -- cannot verify
download!'; \  
exit 1; \  
fi; \  
\  
apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
gnupg \  
openssl \  
tar \  
; \  
\  
wget -O logstash.tar.gz "$LOGSTASH_TARBALL"; \  
\  
if [ "$LOGSTASH_TARBALL_SHA1" ]; then \  
echo "$LOGSTASH_TARBALL_SHA1 *logstash.tar.gz" | sha1sum -c -; \  
fi; \  
\  
if [ "$LOGSTASH_TARBALL_ASC" ]; then \  
wget -O logstash.tar.gz.asc "$LOGSTASH_TARBALL_ASC"; \  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY"; \  
gpg --batch --verify logstash.tar.gz.asc logstash.tar.gz; \  
rm -r "$GNUPGHOME" logstash.tar.gz.asc; \  
fi; \  
\  
dir="$(dirname "$LOGSTASH_PATH")"; \  
\  
mkdir -p "$dir"; \  
tar -xf logstash.tar.gz --strip-components=1 -C "$dir"; \  
rm logstash.tar.gz; \  
\  
apk del .fetch-deps; \  
\  
export LS_SETTINGS_DIR="$dir/config"; \  
# if the "log4j2.properties" file exists (logstash 5.x), let's empty it out so
we get the default: "logging only errors to the console"  
if [ -f "$LS_SETTINGS_DIR/log4j2.properties" ]; then \  
cp "$LS_SETTINGS_DIR/log4j2.properties"
"$LS_SETTINGS_DIR/log4j2.properties.dist"; \  
truncate -s 0 "$LS_SETTINGS_DIR/log4j2.properties"; \  
fi; \  
\  
# set up some file permissions  
for userDir in \  
"$dir/config" \  
"$dir/data" \  
; do \  
if [ -d "$userDir" ]; then \  
chown -R stakater:stakater "$userDir"; \  
fi; \  
done; \  
\  
logstash --version  
  
# Add Defualt logstash config  
ADD ./config/default-logstash.conf /etc/logstash/conf.d/logstash.conf  
  
# expose default config folder  
VOLUME /etc/logstash/conf.d  
  
# Simulate cmd behavior via environment variable  
# So that users are able to provice command line arguments to logstash  
ENV COMMAND "logstash -f /etc/logstash/conf.d/logstash.conf"  
# Make daemon service dir for logstash and place file  
# It will be started and maintained by the base image  
RUN mkdir -p /etc/service/logstash  
ADD start.sh /etc/service/logstash/run  
  
# Use base image's entrypoint

