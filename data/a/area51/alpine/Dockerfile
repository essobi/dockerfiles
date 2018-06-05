################################################################################  
# Base image for all of our Alpine based images.  
#  
# It includes GLIBC in the build  
#  
################################################################################  
FROM alpine:latest  
MAINTAINER Peter Mount <peter@retep.org>  
  
ENV GLIBC_VERSION 2.23-r1  
  
RUN apk add --update curl &&\  
curl -o glibc.apk \  
-L "https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-${GLIBC_VERSION}.apk" && \  
apk add --allow-untrusted glibc.apk && \  
curl -o glibc-bin.apk \  
-L "https://github.com/andyshinn/alpine-pkg-glibc/releases/download/${GLIBC_VERSION}/glibc-bin-${GLIBC_VERSION}.apk" && \  
apk add --allow-untrusted glibc-bin.apk && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc/usr/lib && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
rm -f glibc.apk glibc-bin.apk && \  
rm -rf /var/cache/apk/*  

