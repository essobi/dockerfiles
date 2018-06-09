FROM alpine:3.6  
ARG TS3_VERSION=3.2.0  
ARG TS3_ARCH=amd64  
ARG GLIBC_VERSION=2.27-r0  
  
# Build-time metadata as defined at http://label-schema.org  
ARG BUILD_DATE  
ARG VCS_REF  
LABEL org.label-schema.build-date=$BUILD_DATE \  
org.label-schema.name="docker-teamspeak" \  
org.label-schema.description="TeamSpeak 3 Server Docker Image" \  
org.label-schema.vcs-ref=$VCS_REF \  
org.label-schema.vcs-url="https://github.com/svengo/docker-teamspeak" \  
org.label-schema.vendor="Sven Gottwald" \  
org.label-schema.version=$TS3_VERSION \  
org.label-schema.schema-version="1.0"  
  
ADD https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub /etc/apk/keys/sgerrand.rsa.pub  
ADD https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk /tmp/  
ADD
http://dl.4players.de/ts/releases/${TS3_VERSION}/teamspeak3-server_linux_${TS3_ARCH}-${TS3_VERSION}.tar.bz2
/tmp/  
  
WORKDIR /tmp/  
RUN apk add --update --no-cache bzip2 su-exec bash curl && \  
apk add /tmp/glibc-${GLIBC_VERSION}.apk && \  
tar jxf /tmp/teamspeak3-server_linux_${TS3_ARCH}-${TS3_VERSION}.tar.bz2 && \  
mv /tmp/teamspeak3-server_linux_${TS3_ARCH} /teamspeak && \  
rm -rf /tmp/* && \  
apk del bzip2  
  
WORKDIR /  
  
RUN addgroup -S teamspeak && \  
adduser -h /teamspeak -G teamspeak -S -D teamspeak && \  
chown -R teamspeak:teamspeak /teamspeak  
  
VOLUME ["/data"]  
  
COPY docker-entry-point.sh /entrypoint.sh  
ENTRYPOINT ["/entrypoint.sh"]  
  
EXPOSE 9987/udp 10011 30033  
CMD ["ts3server"]  
  
HEALTHCHECK \--interval=5m --timeout=3s CMD echo quit | curl -sS
telnet://localhost:10011 || exit 1  

