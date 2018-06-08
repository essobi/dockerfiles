FROM alpine:edge  
  
MAINTAINER Yury Evtikhov <yury@evtikhov.info>  
  
ENV PACKAGES="mysql-client" \  
LIB_PACKAGES="glib-dev mariadb-dev zlib-dev pcre-dev libressl-dev" \  
BUILD_PACKAGES="cmake build-base git" \  
BUILD_PATH="/opt/mydumper-src/"  
RUN apk --no-cache add \  
$PACKAGES \  
$BUILD_PACKAGES \  
$LIB_PACKAGES \  
&& \  
git clone https://github.com/maxbube/mydumper.git $BUILD_PATH && \  
cd $BUILD_PATH && \  
cmake . && \  
make && \  
mv ./mydumper /usr/bin/. && \  
mv ./myloader /usr/bin/. && \  
cd / && rm -rf $BUILD_PATH && \  
apk del $BUILD_PACKAGES && \  
rm -f /usr/lib/*.a && \  
(rm "/tmp/"* 2>/dev/null || true) && \  
(rm -rf /var/cache/apk/* 2>/dev/null || true)  
  
CMD ["/usr/sbin/crond", "-f", "-L", "8"]  
  

