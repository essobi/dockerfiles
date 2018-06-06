FROM alpine:3.3  
MAINTAINER Nigel Banks <nigel.g.banks@gmail.com>  
  
LABEL "License"="MIT" \  
"Version"="0.0.1"  
  
ARG S6_VERSION="1.17.1.2"  
ARG GLIBC_VERSION="2.22-r8"  
ARG CONFD_VERSION="0.11.0"  
ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2  
# Install glibc, currently we're not including glibc-bin or glibc-i18.  
#  
# Also we install a few utilities that are used in pretty much all of our
other  
# containers (curl, etc).  
RUN apk --update add openssl ca-certificates libssh2 curl && \  
curl -L -o /tmp/glibc-${GLIBC_VERSION}.apk \  
https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk && \  
apk add --allow-untrusted /tmp/glibc-${GLIBC_VERSION}.apk && \  
curl -L https://github.com/just-
containers/s6-overlay/releases/download/v${S6_VERSION}/s6-overlay-amd64.tar.gz
| \  
tar -xzf - -C / && \  
curl -L -o /usr/local/bin/confd
https://github.com/kelseyhightower/confd/releases/download/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-
amd64 && \  
chmod a+x /usr/local/bin/confd && \  
rm -rf /tmp/* && \  
rm -rf /var/cache/apk/* && \  
rm -fr /root/.cache/* && \  
echo '' > /root/.ash_history  
  
# Start s6  
ENTRYPOINT [ "/init" ]  
  
COPY rootfs /  

