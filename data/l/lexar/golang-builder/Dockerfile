FROM alpine:3.2  
RUN apk update && \  
apk add \  
go \  
git && \  
rm -rf /var/cache/apk/*  
  
RUN mkdir -p /go/src /go/bin  
  
ENV GOPATH /go  
ENV PATH /go/bin:$PATH  
  
WORKDIR /go  

