# Multi-stage build  
# - use golang official image as builder.  
FROM golang:alpine as builder  
  
# Set version of dnscrypt-proxy.  
# without any value, using master branch as default.  
ARG VERSION  
  
# Set go-lang env  
ARG GOOS=linux  
ARG GOARCH=amd64  
  
# Option about UPX  
ARG ENABLE_UPX=true  
ARG UPX_COMP_RATIO=brute  
  
# Install package  
RUN apk --no-cache --update add git upx  
  
# Clone dnscrypt-proxy repo  
RUN git clone -b ${VERSION:-master} https://github.com/jedisct1/dnscrypt-proxy
src  
  
# Set WORKDIR & Start build  
WORKDIR /go/src/dnscrypt-proxy  
  
RUN set -ex \  
&& go clean \  
&& go build -ldflags="-s -w" -o /app/dnscrypt-proxy \  
&& cp /go/src/dnscrypt-proxy/example-* /app  
  
# Set WORKDIR  
WORKDIR /app  
  
# Execute UPX if enabled.  
RUN set -ex ; \  
if [[ $ENABLE_UPX == 'true' ]]; then \  
upx ${UPX_COMP_RATIO:+--$UPX_COMP_RATIO} dnscrypt-proxy ; \  
fi  
  
# Smallest base image  
FROM alpine:latest  
  
MAINTAINER Alto <alto@pendragon.kr>  
  
ARG VERSION  
  
# Select servers  
ENV SERVER_NAMES='cloudflare, google' \  
  
# Enable & Disable protocols  
PROTO_DNSCRYPT='true' \  
PROTO_DOH='true' \  
  
# Check ( DNSSEC & No-logging & No-filter ) option of dns-resolver  
REQUIRE_DNSSEC='false' \  
REQUIRE_NOLOG='true' \  
REQUIRE_NOFILTER='true' \  
  
# Fallback DNS server  
FALLBACK_RESOLVER=1.1.1.1:53 \  
  
# Listen addresses  
LISTEN_ADDRESSES=0.0.0.0:53 \  
  
# Disable auto-regenerate config file on boot.  
ENABLE_AUTO_CONFIG='true' \  
  
# Set version.  
VERSION=${VERSION:-default}  
  
COPY /rootfs /  
  
COPY \--from=builder /app /app  
  
VOLUME /data  
  
RUN set -ex \  
&& apk --no-cache --update add \  
tini \  
ca-certificates \  
&& chmod +x /app/dnscrypt-proxy \  
&& chmod +x /entrypoint.sh  
  
WORKDIR /app  
  
EXPOSE 53/tcp 53/udp  
  
ENTRYPOINT ["/sbin/tini", "--", "/entrypoint.sh"]

