FROM alpine:3.7  
MAINTAINER Jordan Clark jordan.clark@esu10.org  
  
ENV S6_OVERLAY_VERSION 1.21.2.1  
ENV S6_OVERLAY_MD5HASH 45c284a433d95e54f6fbef7cc6fdeee7  
  
COPY container-files /  
  
RUN apk add --no-cache wget ca-certificates && \  
apk --no-cache --update upgrade && \  
cd /tmp && \  
wget https://github.com/just-
containers/s6-overlay/releases/download/v$S6_OVERLAY_VERSION/s6-overlay-
amd64.tar.gz && \  
echo "$S6_OVERLAY_MD5HASH *s6-overlay-amd64.tar.gz" | md5sum -c - && \  
tar xzf s6-overlay-amd64.tar.gz -C / && \  
rm s6-overlay-amd64.tar.gz  
  
ENTRYPOINT ["/init"]  

