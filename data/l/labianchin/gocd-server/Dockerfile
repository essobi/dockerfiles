# Build using: docker build -t labianchin/gocd-server .  
FROM java:openjdk-7-jre  
  
# Warning: this is still a work in progress!!!  
  
# some inspiration:
https://github.com/jenkinsci/docker/blob/02721aab9775f4f26fb23cbf204d1eb5b23d07ea/Dockerfile  
# https://github.com/gocd/gocd-docker/blob/master/Dockerfile.gocd-server  
# https://github.com/docker-
library/redis/blob/94e9dcaaa93312651e91815fe7e4c5ef0f266408/2.6/Dockerfile  
  
ENV GOCD_HOME /var/go  
  
RUN groupadd -r go \  
&& useradd -r -c "Go User" -g "go" -d "$GOCD_HOME" -u 1000 -m -s /bin/bash go
\  
&& mkdir -p /var/lib/go-server/addons /var/log/go-server /etc/go /go-addons \  
&& touch /etc/go/postgresqldb.properties \  
&& chown -R go:go /var/lib/go-server /etc/go /go-addons  
  
ENV GOCD_VERSION=15.2.0-2248  
ENV GOCD_SERVER_SHA1=63847ce16d559e9cb4d2204ead64b9bccc72fe6e  
ENV GOCD_SERVER_URL=https://download.go.cd/gocd-deb/go-
server-$GOCD_VERSION.deb  
RUN set -x \  
&& curl -fSL "$GOCD_SERVER_URL" -o go-server.deb \  
&& echo "$GOCD_SERVER_SHA1 go-server.deb" | sha1sum -c \- \  
&& dpkg -i --debug=10 go-server.deb \  
&& rm go-server.deb \  
&& ln -sf /dev/stdout /var/log/go-server/go-server.log  
  
VOLUME ["/var/lib/go-server", "/etc/go", "/go-addons"]  
# keeping this after volume to set the currect permissions  
RUN chown -R go:go /var/log/go-server /var/lib/go-server /etc/go /go-addons  
EXPOSE 8153 8154  
  
USER go  
  
ENV MANUAL_SETTING=Y  
ENV GO_SERVER_PORT=8153  
ENV GO_SERVER_SSL_PORT=8154  
ENV SERVER_WORK_DIR=/var/lib/go-server  
ENV DAEMON=N  
ENV JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre  
  
CMD ["/usr/share/go-server/server.sh"]

