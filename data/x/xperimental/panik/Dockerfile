FROM golang:1.9 AS builder  
  
ENV CGO_ENABLED=0  
RUN apt-get update && apt-get install -y upx  
  
RUN mkdir -p /go/src/github.com/xperimental/panik  
WORKDIR /go/src/github.com/xperimental/panik  
  
COPY . /go/src/github.com/xperimental/panik  
  
RUN export VERSION="$(git describe --tags --always)"  
  
ENV LD_FLAGS="-w -X main.Version=${VERSION}"  
RUN go get -d -v .  
RUN go install -a -v -tags netgo -ldflags "${LD_FLAGS}" .  
RUN upx -9 /go/bin/panik  
  
FROM scratch  
MAINTAINER Robert Jacob <xperimental@solidproject.de>  
EXPOSE 8080  
COPY \--from=builder /go/bin/panik /panik  
ENTRYPOINT ["/panik"]

