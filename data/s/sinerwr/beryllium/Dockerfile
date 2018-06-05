FROM golang:alpine  
  
MAINTAINER sine "sinerwr@gmail.com"  
RUN apk --update add git && \  
go-wrapper download github.com/SiCo-Ops/Be && \  
cd $GOPATH/src/github.com/SiCo-Ops/Be && \  
apk del git && \  
go-wrapper install && \  
cd $GOPATH/bin &&\  
rm -rf $GOPATH/src  
  
EXPOSE 6666  
WORKDIR $GOPATH/bin  
  
CMD ["Be"]

