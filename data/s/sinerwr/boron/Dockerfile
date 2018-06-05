FROM golang:alpine  
  
MAINTAINER sine "sinerwr@gmail.com"  
RUN apk --update add git && \  
go-wrapper download github.com/SiCo-Ops/B && \  
cd $GOPATH/src/github.com/SiCo-Ops/B && \  
apk del git && \  
go-wrapper install && \  
wget http://s3.amazonaws.com/sico-ops/config.sample.json -O
$GOPATH/bin/config.json && \  
cd $GOPATH/bin &&\  
rm -rf $GOPATH/src  
  
EXPOSE 6666  
WORKDIR $GOPATH/bin  
  
CMD ["B"]

