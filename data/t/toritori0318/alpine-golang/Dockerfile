FROM gliderlabs/alpine:latest  
  
MAINTAINER TSUYOSHI TORII toritori0318  
  
RUN apk update && \  
apk add curl git mercurial openssh-client ca-certificates go \  
bash wget tar gzip rsync && \  
rm /var/cache/apk/*  
  
ENV GOPATH /go  
ENV PATH $GOPATH/bin:/usr/src/go/bin:$PATH  
RUN mkdir -p "$GOPATH/src" "$GOPATH/bin" && chmod -R 777 "$GOPATH"  
WORKDIR $GOPATH  

