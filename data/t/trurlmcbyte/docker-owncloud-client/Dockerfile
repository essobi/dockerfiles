FROM alpine:latest  
  
#RUN cp /etc/apk/repositories /etc/apk/repositories.orig \  
# && echo http://dl-4.alpinelinux.org/alpine/edge/testing >>
/etc/apk/repositories \  
# && apk add --no-cache \  
# curl owncloud-client  
  
ENV VERSION=2.3.3 \  
QTKC_VERSION=0.7.0  
  
RUN apk add --no-cache --virtual .build-deps \  
cmake \  
qt5-qttools-dev \  
qt5-qtwebkit-dev \  
git \  
alpine-sdk \  
&& mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& curl -s
https://codeload.github.com/frankosterfeld/qtkeychain/tar.gz/v$QTKC_VERSION |
tar -xz \  
&& cd qtkeychain-$QTKC_VERSION \  
&& cmake \  
-DCMAKE_INSTALL_PREFIX=/usr \  
-DCMAKE_INSTALL_LIBDIR=lib \  
-DCMAKE_INSTALL_LIBEXECDIR=lib/qtkeychain \  
-DCMAKE_BUILD_TYPE=Release \  
&& make \  
&& make install \  
&& cd /usr/local/src \  
&& curl -s https://codeload.github.com/owncloud/client/tar.gz/v$VERSION | tar
-xz \  
&& cd client-$VERSION \  
&& cmake \  
-DCMAKE_BUILD_TYPE="Release" \  
-DCMAKE_INSTALL_LIBDIR=lib \  
-DCMAKE_INSTALL_PREFIX=/usr \  
-DCMAKE_INSTALL_SYSCONFDIR=/etc/owncloud-client \  
&& make \  
&& cp bin/owncloudcmd /usr/bin/owncloudcmd \  
&& mv src/libsync/libowncloudsync.so* /usr/lib/ \  
&& mv csync/src/libocsync.so* /usr/lib/ \  
&& runDeps="$( \  
scanelf --needed --nobanner /usr/bin/owncloudcmd /usr/lib/libowncloudsync.so
/usr/lib/libowncloudsync.so.$VERSION \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --no-cache --virtual .rundeps $runDeps \  
&& apk del --no-cache .build-deps \  
&& rm -rf /usr/local/src  
  
ADD startup.sh /startup.sh  
  
CMD [ "/startup.sh" ]  

