FROM ryayon/alpine:latest  
  
MAINTAINER Rudy YAYON <ryayon@outlook.com>  
  
# Glibc Version @ https://github.com/sgerrand/alpine-pkg-glibc/releases/  
ENV GLIBC_VERSION 2.26-r0  
  
# Glibc installation as per https://github.com/sgerrand/alpine-pkg-glibc  
RUN apk add --no-cache libstdc++ && \  
wget -q -O /etc/apk/keys/sgerrand.rsa.pub
https://raw.githubusercontent.com/sgerrand/alpine-pkg-
glibc/master/sgerrand.rsa.pub && \  
for pkg in glibc-${GLIBC_VERSION} glibc-bin-${GLIBC_VERSION}
glibc-i18n-${GLIBC_VERSION}; do wget -q -O /tmp/${pkg}.apk
https://github.com/andyshinn/alpine-pkg-
glibc/releases/download/${GLIBC_VERSION}/${pkg}.apk; done && \  
apk add --allow-untrusted /tmp/*.apk && \  
rm -v /tmp/*.apk && \  
/usr/glibc-compat/sbin/ldconfig /lib /usr/glibc-compat/lib  

