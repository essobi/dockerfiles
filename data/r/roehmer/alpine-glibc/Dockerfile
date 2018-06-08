FROM alpine:3.7  
  
LABEL maintainer matt.s.giles@gmail.com  
  
ENV ALPINE_GLIBC_REPO=https://github.com/sgerrand/alpine-pkg-
glibc/releases/download \  
ALPINE_GLIBC_KEY=https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub \  
ALPINE_GLIBC_VSN=2.26-r0 \  
ALPINE_GLIBC_PKGS="glibc-2.26-r0.apk glibc-bin-2.26-r0.apk
glibc-i18n-2.26-r0.apk" \  
BUILD_PKGS="ca-certificates wget"  
RUN \  
apk add \--no-cache --virtual .build-deps $BUILD_PKGS && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub $ALPINE_GLIBC_KEY && \  
wget $ALPINE_GLIBC_REPO/$ALPINE_GLIBC_VSN/glibc-$ALPINE_GLIBC_VSN.apk && \  
wget $ALPINE_GLIBC_REPO/$ALPINE_GLIBC_VSN/glibc-bin-$ALPINE_GLIBC_VSN.apk && \  
wget $ALPINE_GLIBC_REPO/$ALPINE_GLIBC_VSN/glibc-i18n-$ALPINE_GLIBC_VSN.apk &&
\  
apk add \--no-cache $ALPINE_GLIBC_PKGS && \  
/usr/glibc-compat/bin/localedef -i en_US -f UTF-8 en_US.UTF-8 || true && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
apk del glibc-i18n .build-deps && \  
rm $ALPINE_GLIBC_PKGS /etc/apk/keys/sgerrand.rsa.pub /root/.wget-hsts  

