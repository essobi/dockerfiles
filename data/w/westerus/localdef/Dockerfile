#  
# Build: docker build -t localdef .  
# Run: docker run --rm -ti --name alpinelocaldef westerus/localdef:alpine-
latest  
#  
FROM alpine:latest  
MAINTAINER Westerus <westerus@gmail.com>  
LABEL Description="This image is enabled locales language" \  
Version="3.4"  
  
ARG PKG_FLAGS_COMMON="-q"  
ARG PKG_FLAGS_PERSISTANT="${PKG_FLAGS_COMMON} \--clean-protected --no-cache"  
ARG PKG_FLAGS_DEV="${PKG_FLAGS_COMMON} \--no-cache"  
  
ARG PKGUPDATE="apk ${PKG_FLAGS_COMMON} update"  
ARG PKGUPGRADE="apk ${PKG_FLAGS_PERSISTANT} upgrade"  
ARG DELTEMP="rm -rf /var/tmp/* /tmp/*"  
ARG PKGINSTALL="apk ${PKG_FLAGS_PERSISTANT} add"  
ARG PKGREMOVE="apk ${PKG_FLAGS_COMMON} \--purge del"  
ARG GLIBCV="2.23-r3"  
ARG GLIBCURL="https://github.com/sgerrand/alpine-pkg-
glibc/releases/download/${GLIBCV}"  
  
ENV IDIOM="es_ES" TZ="Europe/Madrid"  
ARG LOCALDEF="localedef -i ${IDIOM} -f UTF-8 ${IDIOM}.UTF-8"  
ENV PATH="/sbin:/bin:/usr/sbin:/usr/bin:/usr/local/bin" \  
HOME="/root" TERM=xterm  
  
ADD ${GLIBCURL}/sgerrand.rsa.pub /etc/apk/keys/sgerrand.rsa.pub  
ADD ${GLIBCURL}/glibc-${GLIBCV}.apk /tmp  
ADD ${GLIBCURL}/glibc-bin-${GLIBCV}.apk /tmp  
ADD ${GLIBCURL}/glibc-i18n-${GLIBCV}.apk /tmp  
  
RUN $PKGUPDATE && $PKGUPGRADE && $PKGINSTALL ca-certificates /tmp/glibc* && \  
ln -s /usr/glibc-compat/bin/localedef /usr/bin/localedef && \  
$LOCALDEF && $PKGREMOVE ca-certificates && $DELTEMP  
  
ENV LANG ${IDIOM}.UTF-8  

