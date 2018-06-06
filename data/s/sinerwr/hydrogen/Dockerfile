FROM golang:alpine  
  
MAINTAINER sine "sinerwr@gmail.com"  
RUN apk --update add git && \  
go-wrapper download github.com/SiCo-Ops/H && \  
cd $GOPATH/src/github.com/SiCo-Ops/H && \  
apk del git && \  
go-wrapper install && \  
cp *.json $GOPATH/bin/ && \  
cd $GOPATH/bin &&\  
rm -rf $GOPATH/src  
  
EXPOSE 2048  
WORKDIR $GOPATH/bin  
  
CMD ["H"]

