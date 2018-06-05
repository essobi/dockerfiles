FROM hikarushindo/alpine:3.5  
MAINTAINER Pascal Nitsche  
  
ENV ZNC_VERSION 1.6.4  
ENV GPG_KEYS 5AE420CC0209989E  
  
RUN adduser -S znc && addgroup -S znc  
  
RUN set -ex && \  
\  
apk add --no-cache sudo ca-certificates && \  
update-ca-certificates && \  
\  
apk add --no-cache --virtual .build-deps curl gnupg tar build-base pkgconf
swig icu-dev perl-dev libressl-dev c-ares-dev cyrus-sasl-dev python3-dev tcl-
dev && \  
\  
mkdir -p /usr/src/znc && \  
curl -o znc.tar.gz -L
"http://znc.in/releases/archive/znc-${ZNC_VERSION}.tar.gz" && \  
curl -o znc.tar.gz.sig -L
"http://znc.in/releases/archive/znc-${ZNC_VERSION}.tar.gz.sig" && \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "${GPG_KEYS}" && \  
gpg --batch --verify znc.tar.gz.sig znc.tar.gz && \  
tar --strip-components=1 -xzf znc.tar.gz -C /usr/src/znc && \  
\  
cd /usr/src/znc && \  
./configure --enable-cyrus \  
\--enable-perl \  
\--enable-python \  
\--enable-swig \  
\--enable-tcl && \  
make && \  
make install && \  
cd $HOME && \  
RUNTIME_PACKAGES="$( \  
scanelf --needed --nobanner /usr/local/bin/znc \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" && \  
apk add --no-cache ${RUNTIME_PACKAGES} && \  
\  
apk del --purge .build-deps && \  
rm -rf *.tar.gz* /usr/src /tmp/* /root/.gnupg  
  
COPY docker-entrypoint.sh /usr/local/bin/  
COPY znc.conf.default /znc.conf.default  
  
ENTRYPOINT ["docker-entrypoint.sh"]  
  
VOLUME /znc-data  
  
EXPOSE 6667  
CMD [""]  

