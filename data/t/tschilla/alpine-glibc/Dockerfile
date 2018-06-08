FROM tschilla/alpine:3.7  
  
MAINTAINER Henning Teek <henning.teek@gmail.com>  
  
# language and glibc version  
ENV LANG=C.UTF-8  
ENV GLIBC_VERSION=2.27-r0  
  
# install dependencies and glibc  
RUN apk update && apk upgrade && \  
apk add --no-cache ca-certificates && \  
curl -sSL https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub -o /etc/apk/keys/sgerrand.rsa.pub && \  
for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}
glibc-i18n-${GLIBC_VERSION}; do curl -sSL https://github.com/sgerrand/alpine-
pkg-glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk -o /tmp/${pkg}.apk;
done && \  
apk add /tmp/*.apk && rm -v /tmp/*.apk && \  
( /usr/glibc-compat/bin/localedef --force --inputfile POSIX --charmap UTF-8
C.UTF-8 || true ) && \  
echo "export LANG=C.UTF-8" > /etc/profile.d/locale.sh && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib && \  
apk del glibc-i18n && \  
rm -rf /tmp/* /var/cache/apk/*  

