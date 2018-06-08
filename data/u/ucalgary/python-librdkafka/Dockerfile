FROM python:3.6.5-alpine3.7  
  
ARG LIBRDKAFKA_NAME="librdkafka"  
ARG LIBRDKAFKA_VER="0.11.4"  
# Install librdkafka  
RUN apk add --no-cache --virtual .fetch-deps \  
ca-certificates \  
libressl \  
curl \  
tar && \  
\  
BUILD_DIR="$(mktemp -d)" && \  
\  
curl -sLo "$BUILD_DIR/$LIBRDKAFKA_NAME.tar.gz"
"https://github.com/edenhill/librdkafka/archive/v$LIBRDKAFKA_VER.tar.gz" && \  
mkdir -p $BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER && \  
tar \  
\--extract \  
\--file "$BUILD_DIR/$LIBRDKAFKA_NAME.tar.gz" \  
\--directory "$BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER" \  
\--strip-components 1 && \  
\  
apk add --no-cache --virtual .build-deps \  
bash \  
g++ \  
libressl-dev \  
make \  
musl-dev \  
zlib-dev && \  
\  
cd "$BUILD_DIR/$LIBRDKAFKA_NAME-$LIBRDKAFKA_VER" && \  
./configure \  
\--prefix=/usr && \  
make -j "$(getconf _NPROCESSORS_ONLN)" && \  
make install && \  
\  
runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/local \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add --no-cache --virtual .librdkafka-rundeps \  
$runDeps && \  
\  
cd / && \  
apk del .fetch-deps .build-deps && \  
rm -rf $BUILD_DIR  
  
LABEL maintainer="King Chung Huang <kchuang@ucalgary.ca>" \  
org.label-schema.vcs-url="https://github.com/ucalgary/docker-python-
librdkafka"  

