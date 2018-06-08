FROM alpine:3.2  
MAINTAINER Jonathon W. Marshall "jonathon@gallop.io"  
  
RUN apk --update add git go && rm -rf /var/cache/apk/*  
RUN mkdir -p /usr/lib/gopath  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /usr/lib/gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  

