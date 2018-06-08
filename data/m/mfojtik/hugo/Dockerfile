FROM golang:alpine  
  
MAINTAINER Michal Fojtik <mi@mifo.sk>  
  
LABEL io.openshift.s2i.scripts-url=image:///usr/libexec/s2i  
  
EXPOSE 8080  
RUN mkdir -p /opt/app-root/src/static && \  
chmod -R og+rwx /opt/app-root && \  
chown -R 1001:0 /opt/app-root && \  
mkdir -p /usr/libexec/s2i  
  
WORKDIR /opt/app-root/src  
  
RUN apk add --update git mercurial binutils && \  
go get -v -u github.com/spf13/hugo && \  
strip /go/bin/hugo && \  
apk del git mercurial binutils && \  
rm -rf /go/src /go/pkg  
  
COPY ./s2i/* /usr/libexec/s2i/  
USER 1001  

