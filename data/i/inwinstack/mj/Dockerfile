FROM golang:1.9-alpine AS build-env  
ENV GOPATH "/go"  
ADD . /go/src/github.com/inwinstack/MJ  
RUN apk add --no-cache make git gcc && \  
cd /go/src/github.com/inwinstack/MJ && \  
make deps && make  
  
# Run stage  
FROM alpine  
MAINTAINER Kyle Bai(kyle.b@inwinstack.com)  
  
COPY \--from=build-env /go/src/github.com/inwinstack/MJ/out/MJ /bin/MJ  
RUN apk add --no-cache ca-certificates && \  
rm -f /var/cache/apk/*  
  
ENTRYPOINT ["/bin/MJ"]  

