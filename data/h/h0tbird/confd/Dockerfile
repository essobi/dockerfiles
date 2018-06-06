#------------------------------------------------------------------------------  
# Set the base image for subsequent instructions:  
#------------------------------------------------------------------------------  
FROM alpine:3.3  
MAINTAINER Marc Villacorta Morera <marc.villacorta@gmail.com>  
  
#------------------------------------------------------------------------------  
# Environment variables:  
#------------------------------------------------------------------------------  
ENV CONFD_VERSION="0.11.0" \  
CONFD_URL="https://github.com/kelseyhightower/confd/releases/download" \  
ALPINE_GLIBC_URL="https://circle-artifacts.com/gh/andyshinn/alpine-pkg-
glibc/6/artifacts/0/home/ubuntu/alpine-pkg-glibc/packages/x86_64/" \  
GLIBC_PKG="glibc-2.21-r2.apk" \  
GLIBC_BIN_PKG="glibc-bin-2.21-r2.apk"  
#------------------------------------------------------------------------------  
# Install:  
#------------------------------------------------------------------------------  
RUN apk add --update -t deps openssl \  
&& apk add --update bash && cd /tmp \  
&& wget ${ALPINE_GLIBC_URL}${GLIBC_PKG} ${ALPINE_GLIBC_URL}${GLIBC_BIN_PKG} \  
&& wget ${CONFD_URL}/v${CONFD_VERSION}/confd-${CONFD_VERSION}-linux-amd64 -O
/bin/confd \  
&& apk add --allow-untrusted ${GLIBC_PKG} ${GLIBC_BIN_PKG} \  
&& /usr/glibc/usr/bin/ldconfig /lib /usr/glibc/usr/lib \  
&& echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf \  
&& chmod +x /bin/confd \  
&& apk del --purge deps \  
&& rm -rf /tmp/* /var/cache/apk/*  
  
#------------------------------------------------------------------------------  
# Entrypoint:  
#------------------------------------------------------------------------------  
ENTRYPOINT ["/bin/confd"]  

