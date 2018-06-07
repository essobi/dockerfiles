FROM golang:alpine  
  
RUN apk add --no-cache curl git  
  
ADD . /go/src/github.com/fankserver/docker-prosody-watchdog  
RUN go get github.com/fankserver/docker-prosody-watchdog/... \  
&& go install github.com/fankserver/docker-prosody-watchdog  
ENTRYPOINT /go/bin/docker-prosody-watchdog

