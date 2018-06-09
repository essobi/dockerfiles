FROM alpine:latest  
MAINTAINER Nobuyuki Matsui <nobuyuki.matsui@gmail.com>  
  
ENV LISTEN_PORT "5001"  
ENV GIN_MODE "release"  
ENV GOROOT=/usr/lib/go \  
GOPATH=/go \  
PATH=$PATH:$GOROOT/bin:$GOPATH/bin  
  
WORKDIR $GOPATH  
  
COPY . /tmp/fiware-mqtt-msgfilter  
  
RUN apk update && \  
apk add --no-cache --virtual .go musl-dev git go && \  
mkdir -p $GOPATH/src/github.com/tech-sketch && \  
mv /tmp/fiware-mqtt-msgfilter $GOPATH/src/github.com/tech-sketch && \  
cd $GOPATH/src/github.com/tech-sketch/fiware-mqtt-msgfilter && \  
go get -u github.com/golang/dep/cmd/dep && \  
$GOPATH/bin/dep ensure && \  
go install github.com/tech-sketch/fiware-mqtt-msgfilter && \  
mv $GOPATH/bin/fiware-mqtt-msgfilter /usr/local/bin && \  
rm -rf $GOPATH && \  
apk del --purge .go  
  
EXPOSE 5001  
ENTRYPOINT ["/usr/local/bin/fiware-mqtt-msgfilter"]  

