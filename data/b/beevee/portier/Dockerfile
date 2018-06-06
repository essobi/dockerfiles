FROM golang:alpine as golang  
WORKDIR /go/src/github.com/beevee/portier  
COPY . .  
RUN apk add --no-cache git mercurial \  
&& go get github.com/kardianos/govendor \  
&& govendor sync \  
&& apk del git mercurial  
# Static build required so that we can safely copy the binary over.  
RUN CGO_ENABLED=0 GOOS=linux go build -a -installsuffix cgo -o /go/bin/portier
github.com/beevee/portier  
  
FROM alpine:latest as alpine  
RUN apk --no-cache add tzdata zip ca-certificates  
WORKDIR /usr/share/zoneinfo  
# -0 means no compression. Needed because go's  
# tz loader doesn't handle compressed data.  
RUN zip -r -0 /zoneinfo.zip .  
  
FROM scratch  
# the program:  
COPY \--from=golang /go/bin/portier /portier  
# the timezone data:  
ENV ZONEINFO /zoneinfo.zip  
COPY \--from=alpine /zoneinfo.zip /  
# the tls certificates:  
COPY \--from=alpine /etc/ssl/certs/ca-certificates.crt /etc/ssl/certs/  
ENTRYPOINT ["/portier"]  

