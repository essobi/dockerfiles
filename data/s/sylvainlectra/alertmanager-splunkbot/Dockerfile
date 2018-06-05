FROM golang:1.10-alpine3.7 as builder  
  
ADD . $GOPATH/src/github.com/sylr/alertmanager-splunkbot  
WORKDIR $GOPATH/src/github.com/sylr/alertmanager-splunkbot  
  
RUN apk update && apk upgrade && apk add \--no-cache git  
  
RUN uname -a  
RUN go version  
  
RUN go build -ldflags "-X main.version=$(git describe --dirty --broken)"  
RUN go install  
  
#
-----------------------------------------------------------------------------  
FROM alpine:3.7  
  
WORKDIR /usr/local/bin  
RUN apk --no-cache add ca-certificates  
RUN apk update && apk upgrade && apk add \--no-cache bash curl  
COPY \--from=builder "/go/bin/alertmanager-splunkbot" .  
  
ENTRYPOINT ["/usr/local/bin/alertmanager-splunkbot"]  

