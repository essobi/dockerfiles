FROM mhart/alpine-node:6.9  
  
ENV GOSU_VERSION 1.9  
RUN set -x \  
&& apk add --no-cache --virtual .gosu-deps \  
dpkg \  
gnupg \  
openssl \  
&& dpkgArch="$(dpkg --print-architecture | awk -F- '{ print $NF }')" \  
&& wget -O /usr/local/bin/gosu
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch"
\  
&& wget -O /usr/local/bin/gosu.asc
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-$dpkgArch.asc"
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg \--keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg \--batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del .gosu-deps  
  
RUN apk add --repository http://dl-3.alpinelinux.org/alpine/edge/community/
\--no-cache runit && \  
adduser -u 1000 -D -s /sbin/nologin app app && \  
mkdir /var/log/app && \  
chown app.app /var/log/app  
  
CMD ["runsvdir", "/etc/service"]  

