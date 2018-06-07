#  
# Dockerfile for hitch  
#  
FROM alpine:latest  
MAINTAINER Samuel X. S. Zeng <i@xlibc.me>  
  
ENV HITCH_VER 1.2.0  
ENV HITCH_URL https://hitch-tls.org/source/hitch-$HITCH_VER.tar.gz  
ENV HITCH_SHA256
cc836bfc6d0593284d0236f004e5ee8fd5e41fc3231d81ab4b69feb7a6b4ac41  
ENV HITCH_FILE hitch-$HITCH_VER.tar.gz  
ENV HITCH_TEMP hitch-$HITCH_VER-build  
  
ENV HITCH_DEPS openssl libev  
ENV BUILD_DEPS curl alpine-sdk openssl-dev libev-dev  
  
RUN set -xe \  
&& apk update \  
&& apk add $HITCH_DEPS $BUILD_DEPS \  
&& mkdir $HITCH_TEMP \  
&& cd $HITCH_TEMP \  
&& curl -sSL $HITCH_URL -o $HITCH_FILE \  
&& echo "$HITCH_SHA256 $HITCH_FILE" | sha256sum -c \  
&& tar -xf $HITCH_FILE \--strip 1 \  
&& ./configure --with-rst2man=/bin/true \  
&& make install \  
&& cd .. \  
&& rm -rf $HITCH_TEMP $HITCH_FILE \  
&& apk del --purge $BUILD_DEPS \  
&& rm -rf /var/cache/apk/*  
  
EXPOSE 8443  
ENTRYPOINT ["hitch"]  

