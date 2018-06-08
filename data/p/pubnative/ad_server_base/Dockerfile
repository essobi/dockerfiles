FROM alpine:edge  
MAINTAINER PubNative Team <team@pubnative.net>  
  
RUN echo "http://dl-4.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories; \  
apk add --update \  
go \  
gcc \  
git \  
libc-dev \  
geoip-dev \  
mercurial \  
bash \  
redis && \  
rm -rf /var/cache/apk/*  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /gopath  
ENV PATH $PATH:$GOROOT/bin:$GOPATH/bin  
  
RUN go get -v github.com/ddollar/forego && \  
go get -v github.com/mattn/gom  

