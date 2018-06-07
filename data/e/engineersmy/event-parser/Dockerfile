FROM golang:1.9 as builder  
WORKDIR /go/src/github.com/engineersmy/event-parser/  
COPY . ./  
RUN make build  
  
FROM alpine:3.6  
MAINTAINER Chee Leong <klrkdekira@gmail.com>  
  
RUN apk update && \  
apk add -u tzdata ca-certificates && \  
rm -rf /var/cache/apk/*  
  
COPY \--from=builder \  
/go/src/github.com/engineersmy/event-parser/dist/event-server \  
/bin/  
  
WORKDIR /data  
EXPOSE 80  
CMD ["event-server"]  

