FROM alpine:edge  
  
ENV TERM="xterm" \  
LANG="C.UTF-8" \  
LC_ALL="C.UTF-8"  
ADD baselayout.tar /  
  
ENV GOSU_VERSION 1.10  
ENV GOREPLACE_VERSION=0.5.4  
RUN set -ex \  
&& echo http://dl-cdn.alpinelinux.org/alpine/edge/community/ >>
/etc/apk/repositories \  
&& /usr/local/bin/apk-upgrade \  
&& /usr/local/bin/apk-install \  
bash \  
ca-certificates \  
openssl \  
&& update-ca-certificates \  
&& /usr/local/bin/generate-dockerimage-info  
  
RUN set -ex; \  
\  
apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
; \  
\  
dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')"; \  
wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch";
\  
wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc";
\  
\  
# verify the signature  
export GNUPGHOME="$(mktemp -d)"; \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4; \  
gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu; \  
rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc; \  
\  
chmod +x /usr/local/bin/gosu; \  
# verify that the binary works  
gosu nobody true; \  
\  
apk del .gosu-deps  
  
RUN set -ex \  
&& wget -O /usr/local/bin/go-replace
https://github.com/webdevops/goreplace/releases/download/$GOREPLACE_VERSION/gr-64-linux
\  
&& chmod +x /usr/local/bin/go-replace \  
&& docker-image-cleanup  

