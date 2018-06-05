FROM
alpine:3.7@sha256:ccba511b1d6b5f1d83825a94f9d5b05528db456d9cf14a1ea1db892c939cda64  
  
ENV CURL_VERSION=7.57.0
CURL_SHA256=c92fe31a348eae079121b73884065e600c533493eb50f1f6cee9c48a3f454826  
  
RUN set -ex; \  
apk add --update --no-cache openssl nghttp2 ca-certificates bash; \  
apk add --update --no-cache --virtual curldeps g++ make perl openssl-dev
nghttp2-dev wget; \  
wget https://curl.haxx.se/download/curl-$CURL_VERSION.tar.bz2; \  
echo "$CURL_SHA256 curl-$CURL_VERSION.tar.bz2" | sha256sum -c; \  
tar xjvf curl-$CURL_VERSION.tar.bz2; \  
rm curl-$CURL_VERSION.tar.bz2; \  
cd curl-$CURL_VERSION; \  
sed -i 's|#define USE_NTLM|/* #define USE_NTLM */|' lib/curl_setup.h; \  
./configure \  
--with-nghttp2=/usr \  
--prefix=/usr \  
--with-ssl \  
--enable-ipv6 \  
--enable-unix-sockets \  
--without-libidn \  
--without-libidn2 \  
--disable-static \  
--disable-ldap \  
--disable-ftp \  
--disable-rtsp \  
--disable-dict \  
--disable-tftp \  
--disable-pop3 \  
--disable-smb \  
--disable-gopher \  
--disable-manual \  
--disable-ntlm-wb \  
--with-pic; \  
make; \  
make install; \  
cd /; \  
rm -r curl-$CURL_VERSION; \  
rm -r /usr/share/man; \  
apk del curldeps; \  
rm -r /var/cache/apk && mkdir /var/cache/apk  
  
ENTRYPOINT ["/usr/bin/curl"]  
  
RUN apk add --update --no-cache jq  

