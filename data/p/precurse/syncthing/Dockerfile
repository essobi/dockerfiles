ARG BASE_IMAGE=alpine:3.7  
FROM ${BASE_IMAGE}  
  
LABEL maintainer "andrewklaus@gmail.com"  
ENV REFRESHED_AT 2017-09-18  
ARG ARCH=amd64  
  
WORKDIR /  
  
ADD VERSION /VERSION  
RUN export VERSION=`cat /VERSION` && apk add --no-cache curl gnupg \  
&& curl -sLO
https://github.com/syncthing/syncthing/releases/download/v${VERSION}/syncthing-
linux-${ARCH}-v${VERSION}.tar.gz \  
&& curl -sLO
https://github.com/syncthing/syncthing/releases/download/v${VERSION}/sha256sum.txt.asc
\  
&& grep syncthing-linux-${ARCH} sha256sum.txt.asc | sha256sum \  
&& gpg --keyserver keyserver.ubuntu.com --recv-key D26E6ED000654A3E \  
&& gpg --verify sha256sum.txt.asc \  
&& tar -zxf syncthing-linux-${ARCH}-v${VERSION}.tar.gz \  
&& mv syncthing-linux-${ARCH}-v${VERSION}/syncthing /syncthing  
  
FROM ${BASE_IMAGE}  
RUN apk --no-cache add ca-certificates  
WORKDIR /  
  
RUN mkdir -p /syncthing /data \  
&& adduser -D -h /var/syncthing -s /nologin syncthing \  
&& chown -R syncthing:syncthing /var/syncthing /data \  
&& chown syncthing /syncthing  
  
COPY \--from=0 /syncthing /syncthing/syncthing  
  
EXPOSE 8384 22000 21027/udp  
  
USER syncthing  
  
# Create vols  
VOLUME /var/syncthing /data  
  
# Disable default folder  
ENV STNODEFAULTFOLDER=1  
HEALTHCHECK \--interval=5m --timeout=3s \  
CMD nc -z localhost 22000 || exit 1  
  
ENTRYPOINT ["/syncthing/syncthing"]  
CMD ["-home", "/var/syncthing", "-gui-address", "0.0.0.0:8384", "-no-browser"]  

