FROM alpine:latest  
  
RUN mkdir /go  
ENV GOPATH /go  
  
RUN \  
apk add --update git go make gcc musl-dev ca-certificates linux-headers && \  
mkdir -p $GOPATH/src/github.com/ethereum && \  
(cd $GOPATH/src/github.com/ethereum && git clone \--branch v1.7.1 --depth=1
https://github.com/ethereum/go-ethereum) && \  
go build -v github.com/ethereum/go-ethereum/cmd/faucet && \  
apk del git go make gcc musl-dev linux-headers && \  
rm -rf $GOPATH && rm -rf /var/cache/apk/*  
  
ADD start.sh /  
  
VOLUME /config  
  
EXPOSE 8080  
CMD ["/bin/sh", "/start.sh"]  

