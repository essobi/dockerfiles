# pushed to docker as slintes/alpine-glibc  
# https://github.com/gliderlabs/docker-alpine  
FROM gliderlabs/alpine:3.2  
  
MAINTAINER Marc Sluiter <marc.sluiter@luminis.eu>  
  
# install common tools  
RUN apk --update add wget curl ca-certificates bash  
  
# java needs glibc  
# see https://github.com/gliderlabs/docker-alpine/issues/11  
  
RUN wget "https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-
glibc/packages/x86_64/glibc-2.21-r2.apk" \  
"https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/glibc-
bin-2.21-r2.apk" && \  
apk add --allow-untrusted glibc-2.21-r2.apk glibc-bin-2.21-r2.apk && \  
/usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm /var/cache/apk/*  

