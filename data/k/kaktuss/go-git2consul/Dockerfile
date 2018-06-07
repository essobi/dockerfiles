FROM golang:alpine AS build  
  
ENV PKG=go-git2consul  
COPY $PKG.go /go/src/$PKG/$PKG.go  
  
RUN \  
apk add --no-cache --virtual .build-deps \  
git \  
  
&& cd /go/src/$PKG \  
&& go get \  
  
&& apk del .build-deps  
  
FROM alpine:3.6  
RUN \  
apk add --no-cache \  
ca-certificates \  
su-exec \  
tzdata  
  
COPY \--from=build /go/bin/$PKG /usr/local/bin/$PKG  
COPY entrypoint.sh /usr/local/bin/entrypoint.sh  
  
ENV USER_UID=1000  
ENV USER_GID=1000  
ENV CONSUL_HTTP_ADDR=  
ENV G2C_PERIOD=300  
ENV G2C_REPO=  
ENV G2C_TARGET=  
  
CMD ["/usr/local/bin/entrypoint.sh"]  

