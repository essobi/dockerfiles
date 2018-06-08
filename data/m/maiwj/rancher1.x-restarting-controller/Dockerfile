#############  
# phase one #  
#############  
FROM golang:1.9.2-alpine3.7 AS builder  
  
RUN apk add --no-cache --update \  
curl \  
git \  
; \  
curl -fsSL -o /usr/local/bin/dep
https://github.com/golang/dep/releases/download/v0.3.2/dep-linux-amd64; \  
chmod +x /usr/local/bin/dep; \  
go get -u github.com/prometheus/promu; \  
git clone https://github.com/thxcode/rancher1.x-restarting-controller.git
$GOPATH/src/github.com/thxcode/rancher1.x-restarting-controller  
  
## build  
RUN cd $GOPATH/src/github.com/thxcode/rancher1.x-restarting-controller; \  
dep ensure -v; \  
$GOPATH/bin/promu build --prefix ./.build; \  
mkdir -p /build; \  
cp -f ./.build/rancher-restarting-controller /build/  
  
#############  
# phase two #  
#############  
FROM alpine:3.7  
  
MAINTAINER Frank Mai <frank@rancher.com>  
  
ARG BUILD_DATE  
ARG VCS_REF  
ARG VERSION  
  
LABEL \  
io.github.thxcode.build-date=$BUILD_DATE \  
io.github.thxcode.name="rancher1.x-restarting-controller" \  
io.github.thxcode.description="A controller of Rancher1.x to manage the
restart action of container." \  
io.github.thxcode.url="https://github.com/thxcode/rancher1.x-restarting-
controller" \  
io.github.thxcode.vcs-type="Git" \  
io.github.thxcode.vcs-ref=$VCS_REF \  
io.github.thxcode.vcs-url="https://github.com/thxcode/rancher1.x-restarting-
controller.git" \  
io.github.thxcode.vendor="Rancher Labs, Inc" \  
io.github.thxcode.version=$VERSION \  
io.github.thxcode.schema-version="1.0" \  
io.github.thxcode.license="MIT" \  
io.github.thxcode.docker.dockerfile="/Dockerfile"  
  
RUN apk add --no-cache --update \  
ca-certificates \  
; \  
mkdir -p /data; \  
chown -R nobody:nogroup /data; \  
mkdir -p /run/cache  
  
COPY --from=builder /build/rancher-restarting-controller /usr/sbin/rancher-
restarting-controller  
  
USER nobody  
  
ENTRYPOINT [ "/usr/sbin/rancher-restarting-controller" ]  

