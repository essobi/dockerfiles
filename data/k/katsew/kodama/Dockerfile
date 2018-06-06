FROM golang:alpine AS build-machine  
  
RUN apk --update add git openssh && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
COPY . /go/src/github.com/katsew/kodama  
  
WORKDIR /go/src/github.com/katsew/kodama  
  
RUN go-wrapper download  
RUN go-wrapper install  
  
FROM alpine:latest  
  
COPY \--from=build-machine /go/bin/kodama /usr/local/bin/kodama  
RUN apk --update add ca-certificates iptables && \  
rm -rf /var/lib/apt/lists/* && \  
rm /var/cache/apk/*  
  
ENTRYPOINT ["/usr/local/bin/kodama"]  
CMD ["http", "server"]  

