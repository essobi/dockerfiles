FROM gliderlabs/alpine:3.1  
  
MAINTAINER Kevin van der Vlist <kvdvlist@sogyo.nl>  
  
RUN apk update \  
&& apk add wget go git gcc libgcc musl-dev \  
&& GOPATH=/go go get github.com/hashicorp/consul \  
&& cd /go/src/github.com/hashicorp/consul \  
&& git checkout v0.5.2 \  
&& cd /bin \  
&& GOPATH=/go go build github.com/hashicorp/consul \  
&& rm -rf /go \  
&& cd /tmp \  
&& wget --no-check-certificate -O ui.zip
https://dl.bintray.com/mitchellh/consul/0.5.2_web_ui.zip \  
&& unzip ui.zip \  
&& mv dist /ui \  
&& rm ui.zip \  
&& apk del wget go git gcc libgcc musl-dev \  
&& rm -rf /var/cache/apk/*  
  
ENV GOMAXPROCS 4  
  
EXPOSE 8300 8301 8301/udp 8302 8302/udp 8400 8500 8600 8600/udp  
  
VOLUME [ "/data", "/config" ]  
  
ENTRYPOINT [ "/bin/consul" ]  
  
CMD []

