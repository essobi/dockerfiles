FROM alpine:3.2  
MAINTAINER Ken Huang <ken@after4u.com>  
  
#basic tools for all alpine image  
RUN apk --update add bash  
  
RUN mkdir /projects  
  
COPY usr/bin/apk-install /usr/bin/apk-install  
RUN chmod 755 /usr/bin/apk-install  
  
# combine docker file frolvlad/alpine-glibc frol/docker-alpine-oraclejdk8  
# Here we use several hacks collected from
https://github.com/gliderlabs/docker-alpine/issues/11:  
# 1. install GLibc (which is not the cleanest solution at all)  
# 2. hotfix /etc/nsswitch.conf, which is apperently required by glibc and is
not used in Alpine Linux  
# Fix DNS resolution issues when nss is not installed  
RUN echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf  
  
# we purposely leave this apk add command here to be separated from the above
apk add command in the hope that one day we no longer need this hack.  
RUN apk --update add ca-certificates && \  
export ALPINE_GLIBC_BASE_URL="https://circle-
artifacts.com/gh/andyshinn/alpine-pkg-glibc/6/artifacts/0/home/ubuntu/alpine-
pkg-glibc/packages/x86_64" && \  
export ALPINE_GLIBC_PACKAGE="glibc-2.21-r2.apk" && \  
export ALPINE_GLIBC_BIN_PACKAGE="glibc-bin-2.21-r2.apk" && \  
wget "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE"
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_BIN_PACKAGE" && \  
apk add --allow-untrusted "$ALPINE_GLIBC_PACKAGE" "$ALPINE_GLIBC_BIN_PACKAGE"
&& \  
/usr/glibc/usr/bin/ldconfig "/lib" "/usr/glibc/usr/lib" && \  
apk del ca-certificates && \  
rm "$ALPINE_GLIBC_PACKAGE" "$ALPINE_GLIBC_BIN_PACKAGE" /var/cache/apk/*  

