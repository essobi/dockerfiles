FROM alpine:3.3  
RUN adduser -h /transfersh -S -u 1000 transfersh  
  
# Straight from https://github.com/docker-
library/rabbitmq/blob/master/Dockerfile#L8  
ENV GOSU_VERSION 1.7  
RUN \  
apk add --no-cache --virtual build.deps curl gnupg \  
&& curl -o /usr/local/bin/gosu -fsSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-amd64" \  
&& curl -o /usr/local/bin/gosu.asc -fsSL
"https://github.com/tianon/gosu/releases/download/$GOSU_VERSION/gosu-
amd64.asc" \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys
B42F6819007F00F88E364FD4036A9C25BF357DD4 \  
&& gpg --batch --verify /usr/local/bin/gosu.asc /usr/local/bin/gosu \  
&& rm -r "$GNUPGHOME" /usr/local/bin/gosu.asc \  
&& chmod +x /usr/local/bin/gosu \  
&& gosu nobody true \  
&& apk del build.deps  
  
ENV TRANSFERSH_VERSION 7986596  
RUN set -x; \  
apk add --no-cache --virtual build.deps go git \  
&& export GOPATH=/go PATH=/go/bin:$PATH \  
&& mkdir -p /go/src/app && cd /go/src/app \  
&& git clone https://github.com/dutchcoders/transfer.sh . \  
&& git checkout $TRANSFERSH_VERSION \  
&& git filter-branch --subdirectory-filter transfersh-server \  
&& go get -v \  
&& go build \  
&& mv app /transfersh/ && mv static /transfersh && chown -R transfersh
/transfersh \  
&& apk del build.deps \  
&& rm -rf /go  
  
WORKDIR "/transfersh"  
  
VOLUME "/data"  
  
EXPOSE 8080  
COPY entrypoint.sh /  
  
ENTRYPOINT ["/entrypoint.sh"]  
  
CMD ["/transfersh/app"]  

