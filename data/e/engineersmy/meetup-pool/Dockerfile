# Builder  
FROM golang:1.10.2 as builder  
WORKDIR /go/src/github.com/engineersmy/meetup-pool/  
COPY . ./  
RUN go get -u -v  
RUN go build  
  
# Image  
FROM alpine:3.7  
RUN apk add --no-cache ca-certificates tzdata  
  
COPY \--from=builder \  
/go/src/github.com/engineersmy/meetup-pool/meetup-pool \  
/bin/  
  
# Our localtime as default  
RUN cp /usr/share/zoneinfo/Asia/Kuala_Lumpur /etc/localtime && \  
echo "Asia/Kuala_Lumpur" > /etc/timezone && \  
apk del tzdata  
  
RUN mkdir -p /data  
  
EXPOSE 80  
WORKDIR /data  
  
CMD [ "meetup-pool" ]

