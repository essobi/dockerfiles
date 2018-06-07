FROM alpine:edge  
MAINTAINER Adrian Hobbs <adrianhobbs@gmail.com>  
ENV PACKAGE "tvheadend tvheadend-dvb-scan libhdhomerun tzdata"  
# Update packages in base image, avoid caching issues by combining statements,
install build software and deps  
RUN echo "http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
apk add \--no-cache $PACKAGE && \  
mkdir -p /config /recordings && \  
chown -R tvheadend:bin /config /recordings && \  
cp /usr/share/zoneinfo/Australia/Sydney /etc/localtime && \  
echo "Australia/Sydney" > /etc/timezone  
  
USER tvheadend  
  
EXPOSE 9981 9982  
  
ENTRYPOINT ["/usr/bin/tvheadend"]  
CMD ["-C","-c","/config"]  
  

