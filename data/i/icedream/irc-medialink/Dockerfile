FROM golang:1.7  
RUN mkdir -p /go/src/app  
WORKDIR /go/src/app  
  
COPY . /go/src/app  
RUN \  
mkdir -p "$GOPATH/src/github.com/icedream" &&\  
ln -sf /go/src/app "$GOPATH/src/github.com/icedream/irc-medialink" &&\  
go-wrapper download &&\  
go-wrapper install  
  
CMD ["go-wrapper", "run"]  

