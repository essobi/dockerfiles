FROM golang:alpine  
  
RUN apk update && \  
apk add git gcc libc-dev && \  
go get github.com/tools/godep && \  
rm -rf /var/cache/apk/* && \  
CGO_ENABLED=0 go install -a std  

