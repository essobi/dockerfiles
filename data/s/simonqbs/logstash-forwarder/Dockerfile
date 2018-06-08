FROM alpine:3.2  
ENV LUMBERJACK_VERSION 0.4.0  
RUN set -x; \  
apk add -U --virtual build-deps go git \  
&& mkdir /go \  
&& export GOPATH=/go PATH=/go/bin:$PATH \  
&& go get -v github.com/elastic/logstash-forwarder \  
&& cd /go/src/github.com/elastic/logstash-forwarder \  
&& git checkout v$LUMBERJACK_VERSION \  
&& go build \  
&& mv logstash-forwarder /usr/local/bin \  
&& apk del build-deps \  
&& rm -rf /go /var/cache/apk/*  
  
WORKDIR /logstash  
  
ENTRYPOINT ["logstash-forwarder"]  

