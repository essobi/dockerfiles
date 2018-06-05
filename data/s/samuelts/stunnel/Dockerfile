#  
# Dockerfile for stunnel  
#  
FROM alpine:latest  
MAINTAINER Samuel X.S Zeng <samuel.zxs@gmail.com>  
  
ENV STUNNEL_VER 5.35  
ENV STUNNEL_URL https://www.stunnel.org/downloads/stunnel-$STUNNEL_VER.tar.gz  
ENV STUNNEL_SHA256
ffa386ae4c825f35f35157c285e7402a6d58779ad8c3822f74a9d355b54aba1d  
ENV STUNNEL_FILE stunnel-$STUNNEL_VER.tar.gz  
ENV STUNNEL_TEMP stunnel-$STUNNEL_VER-build  
ENV STUNNEL_CONF_DIR /etc/stunnel  
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
&& mkdir -p $STUNNEL_CONF_DIR  
  
ENV CFG_FILE $STUNNEL_CONF_DIR/stunnel.conf  
  
CMD ["stunnel", "$CFG_FILE"]  

