# builder image  
FROM golang:alpine as builder  
  
RUN apk add --update git && go get upspin.io/cmd/...  
  
# final image  
FROM alpine  
MAINTAINER Mikkel Oscar Lyderik Larsen <m@moscar.net>  
  
RUN apk add --update ca-certificates  
  
COPY \--from=builder /go/bin/upspinserver /usr/bin/  
  
ENTRYPOINT ["/usr/bin/upspinserver"]  

