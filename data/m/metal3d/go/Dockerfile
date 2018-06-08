FROM alpine:latest  
MAINTAINER Patrice FERLET <metal3d@gmail.com>  
  
RUN set -ex;\  
apk add --update build-base ca-certificates git bzr mercurial curl; \  
rm -rf /var/cache/apk/*  
RUN set -ex; \  
apk add --update go; \  
mkdir /tmp/go1.6; cd /tmp/go1.6; \  
curl https://storage.googleapis.com/golang/go1.6.src.tar.gz >
go1.6.src.tar.gz; \  
tar zxf go1.6.src.tar.gz; \  
cd go/src; \  
GOROOT_BOOTSTRAP=/usr/lib/go sh ./make.bash; \  
apk del --purge go; \  
cd; mv /tmp/go1.6/go /usr/lib/go; \  
rm -rf /go1.6.src.tar.gz /tmp/* /var/cache/apk/*  
  
ENV GOROOT /usr/lib/go  
ENV GOPATH /go  
ENV PATH $GOROOT/bin:$GOPATH/bin:$PATH  
WORKDIR /go  
  
ENTRYPOINT ["go"]  

