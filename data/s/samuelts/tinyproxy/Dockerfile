#  
# Dockerfile for tinyproxy  
#  
FROM alpine:latest  
MAINTAINER Samuel X. S. Zeng <i@xlibc.me>  
  
ENV TP_VER 1.8.4  
ENV TP_URL
https://github.com/tinyproxy/tinyproxy/releases/download/$TP_VER/tinyproxy-$TP_VER.tar.bz2  
ENV TP_FILE tinyproxy-$TP_VER.tar.bz2  
ENV TP_TEMP tinyproxy-$TP_VER-build  
  
ENV BUILD_DEPS curl alpine-sdk asciidoc  
  
RUN set -xe \  
&& apk update \  
&& apk add $BUILD_DEPS \  
&& mkdir $TP_TEMP \  
&& cd $TP_TEMP \  
&& curl -sSL $TP_URL | tar -xj --strip 1 \  
&& ./configure \  
&& make install \  
&& cd .. \  
&& rm -rf $TP_TEMP $TP_FILE \  
&& apk del --purge $BUILD_DEPS \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 8888  
CMD ["tinyproxy", "-d"]  

