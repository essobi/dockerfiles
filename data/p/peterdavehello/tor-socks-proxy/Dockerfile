FROM alpine:3.7  
MAINTAINER Peter Dave Hello <hsu@peterdavehello.org>  
  
RUN echo '@edge http://dl-cdn.alpinelinux.org/alpine/edge/community' >>
/etc/apk/repositories && \  
apk -U upgrade && \  
apk -v add tor@edge curl && \  
rm -rf /var/cache/apk/*  
RUN tor --version  
ADD torrc /etc/tor/  
  
HEALTHCHECK \--timeout=10s --start-period=60s \  
CMD curl --fail --socks5-hostname localhost:9150 -I -L 'https://cdnjs.com/' ||
exit 1  
  
EXPOSE 9150  
CMD /usr/bin/tor -f /etc/tor/torrc  

