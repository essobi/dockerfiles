FROM alpine:latest  
MAINTAINER Nobuyuki Matsui <nobuyuki.matsui@gmail.com>  
  
ENV LISTEN_PORT "3000"  
ENV GIN_MODE "release"  
ENV GOROOT=/usr/lib/go \  
GOPATH=/go \  
PATH=$PATH:$GOROOT/bin:$GOPATH/bin  
  
WORKDIR $GOPATH  
  
COPY . /tmp/fiware-ambassador-auth  
  
RUN apk update && \  
apk add --no-cache --virtual .go musl-dev git go && \  
mkdir -p $GOPATH/src/github.com/tech-sketch && \  
mv /tmp/fiware-ambassador-auth $GOPATH/src/github.com/tech-sketch && \  
cd $GOPATH/src/github.com/tech-sketch/fiware-ambassador-auth && \  
go get -u github.com/golang/dep/cmd/dep && \  
$GOPATH/bin/dep ensure && \  
go install github.com/tech-sketch/fiware-ambassador-auth && \  
mv $GOPATH/bin/fiware-ambassador-auth /usr/local/bin && \  
rm -rf $GOPATH && \  
apk del --purge .go  
  
EXPOSE 3000  
ENTRYPOINT ["/usr/local/bin/fiware-ambassador-auth"]  

