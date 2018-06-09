#  
# Dockerfile for stunnel  
#  
FROM alpine:latest  
MAINTAINER Samuel X. S. Zeng <i@xlibc.me>  
  
ENV STUNNEL_VER 5.32  
ENV STUNNEL_URL https://www.stunnel.org/downloads/stunnel-$STUNNEL_VER.tar.gz  
ENV STUNNEL_SHA256
0ee64774d7a720f3ffd129b08557ee0882704c7f65b859c40e315a175b68a6fd  
ENV STUNNEL_FILE stunnel-$STUNNEL_VER.tar.gz  
ENV STUNNEL_TEMP stunnel-$STUNNEL_VER-build  
ENV STUNNEL_CONF /usr/local/etc/stunnel/stunnel.conf  
ENV STUNNEL_DEPS openssl  
ENV BUILD_DEPS curl alpine-sdk openssl-dev  
  
RUN set -xe \  
&& apk update \  
&& apk add $STUNNEL_DEPS $BUILD_DEPS \  
&& mkdir $STUNNEL_TEMP \  
&& cd $STUNNEL_TEMP \  
&& curl -sSL $STUNNEL_URL -o $STUNNEL_FILE \  
&& echo "$STUNNEL_SHA256 $STUNNEL_FILE" | sha256sum -c \  
&& tar -xf $STUNNEL_FILE \--strip 1 \  
&& ./configure \  
&& make install \  
&& cd .. \  
&& rm -rf $STUNNEL_TEMP $STUNNEL_FILE \  
&& apk --purge del $BUILD_DEPS \  
&& mkdir -p $STUNNEL_CONF  
  
ADD ./stunnel.conf $STUNNEL_CONF/stunnel.conf  
  
ENV CFG_FILE $STUNNEL_CONF/stunnel.conf  
  
CMD ["stunnel", "$CFG_FILE"]  

