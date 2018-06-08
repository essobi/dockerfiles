FROM alpine:3.3  
ADD run-one /usr/bin/run-one  
  
RUN echo "@edge http://nl.alpinelinux.org/alpine/edge/main" >>
/etc/apk/repositories && \  
echo "@community http://nl.alpinelinux.org/alpine/edge/community" >>
/etc/apk/repositories && \  
echo "@testing http://nl.alpinelinux.org/alpine/edge/testing" >>
/etc/apk/repositories && \  
  
# Install minimal packages  
apk update && \  
apk add runit@community wget bzip2 unzip bash tzdata && \  
  
# Set timezone  
cp /usr/share/zoneinfo/UTC /etc/localtime && \  
echo "Etc/UTC" > /etc/timezone && \  
apk del tzdata && \  
  
# Create lo-daemon  
addgroup -g 999 lo-daemon && \  
adduser lo-daemon -D -u 999 -G lo-daemon -S -h /services/ -s /bin/bash && \  
  
# Alpine nsswitch: tells the C lib to look first at the /etc/hosts files  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm -rf /var/cache/apk/*  
  
  
# Set env vars  
ENV LANG=en_US.UTF-8 \  
LC_ALL=en_US.UTF-8  
CMD ["/sbin/runsvdir", "-P", "/etc/sv"]  

