FROM docker:17.12.0-dind  
MAINTAINER Tom Denham <tom@projectcalico.org>  
  
# Install iptables, ip6tables, iproute2, and perform glibc install as per:  
# https://github.com/jeanblanchard/docker-alpine-glibc/blob/master/Dockerfile  
RUN apk add --update iptables ip6tables ipset iproute2 curl busybox-extras &&
\  
curl -o glibc.apk -L "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/2.23-r1/glibc-2.23-r1.apk" && \  
apk add --allow-untrusted glibc.apk && \  
curl -o glibc-bin.apk -L "https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/2.23-r1/glibc-bin-2.23-r1.apk" && \  
apk add --allow-untrusted glibc-bin.apk && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm -f glibc.apk glibc-bin.apk && \  
rm -rf /var/cache/apk/*  
  

