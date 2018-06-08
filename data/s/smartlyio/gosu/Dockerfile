FROM alpine:3.6 AS gosu  
  
ENV GOSU_VERSION 1.10  
RUN set -ex; \  
apk add \--no-cache \--virtual .gosu-deps \  
ca-certificates \  
dpkg \  
gnupg \  
openssl \  
; \  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg \--keyserver ha.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 || \  
gpg \--keyserver eu.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 || \  
gpg \--keyserver ipv6.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 || \  
gpg \--keyserver ipv4.pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 || \  
gpg \--keyserver pool.sks-keyservers.net \--recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
; \  
gpg \--batch \--verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -rf "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
apk del .gosu-deps;  
  
COPY gosu/1.10/alpine/docker-entrypoint.sh /gosu-entrypoint.sh  

