ARG BASE_IMAGE=golang:alpine  
FROM golang:1.9-alpine  
  
LABEL maintainer "andrewklaus@gmail.com"  
ENV REFRESHED_AT 2017-11-11  
ARG ARCH=amd64  
  
WORKDIR /  
  
ADD VERSION /VERSION  
RUN export VERSION=`cat /VERSION` && apk add --no-cache curl \  
&& curl -sLO https://github.com/syncthing/syncthing/archive/v${VERSION}.tar.gz
\  
&& tar -zxf v${VERSION}.tar.gz \  
&& mkdir -p /root/go/src/github.com/syncthing \  
&& mv /syncthing-${VERSION} /root/go/src/github.com/syncthing/syncthing  
  
WORKDIR /root/go/src/github.com/syncthing/syncthing  
  
RUN GOPATH=/root/go go run build.go  
  
FROM alpine:3.7  
RUN apk --no-cache add ca-certificates  
WORKDIR /  
  
RUN mkdir -p /syncthing-relay \  
&& adduser -D -h /var/syncthing-relay -s /nologin syncthing-relay \  
&& chown -R syncthing-relay:syncthing-relay /var/syncthing-relay  
  
COPY \--from=0 /root/go/src/github.com/syncthing/syncthing/bin/strelaysrv
/strelaysrv  
  
EXPOSE 22067 22070  
USER syncthing-relay  
  
# Create vols  
VOLUME /var/syncthing-relay  
  
HEALTHCHECK \--interval=5m --timeout=3s \  
CMD nc -z localhost 22067 || exit 1  
  
ENTRYPOINT ["/strelaysrv","-keys","/var/syncthing-relay"]  
CMD ["-global-rate=1048576","-provided-by=precurse"]  

