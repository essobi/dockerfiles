#BUILDS: teampiggycoin/piggycoind  
FROM qlustor/alpine-runit  
MAINTAINER Team PiggyCoin <team@piggy-coin.com>  
  
# Here we use several hacks collected from
https://github.com/gliderlabs/docker-alpine/issues/11:  
# 1. install GLibc (which is not the cleanest solution at all)  
# 2. hotfix /etc/nsswitch.conf, which is apperently required by glibc and is
not used in Alpine Linux  
# Credits to (Vlad Frolov)[https://github.com/frol/docker-alpine-glibc] for
this fix.  
RUN apk add --no-cache --virtual=build-dependencies wget ca-certificates && \  
export ALPINE_GLIBC_BASE_URL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/2.21-r2" && \  
export ALPINE_GLIBC_PACKAGE="glibc-2.21-r2.apk" && \  
export ALPINE_GLIBC_BIN_PACKAGE="glibc-bin-2.21-r2.apk" && \  
wget "$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_PACKAGE"
"$ALPINE_GLIBC_BASE_URL/$ALPINE_GLIBC_BIN_PACKAGE" && \  
apk add --no-cache --allow-untrusted "$ALPINE_GLIBC_PACKAGE"
"$ALPINE_GLIBC_BIN_PACKAGE" && \  
/usr/glibc/usr/bin/ldconfig "/lib" "/usr/glibc/usr/lib" && \  
echo 'hosts: files mdns4_minimal [NOTFOUND=return] dns mdns4' >>
/etc/nsswitch.conf && \  
apk del build-dependencies && \  
rm "$ALPINE_GLIBC_PACKAGE" "$ALPINE_GLIBC_BIN_PACKAGE"  
  
# Install piggycoind  
ADD . /  
  
EXPOSE 54480-54481  
VOLUME /root/.newpiggycoin  
ENTRYPOINT ["/sbin/runit-docker"]  

