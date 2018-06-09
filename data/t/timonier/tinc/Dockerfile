FROM alpine:latest  
  
LABEL \  
maintainer="Morgan Auchede <morgan.auchede@gmail.com>"  
  
ENV \  
TINC_VERSION=latest  
  
RUN set -ex \  
\  
# Install packages  
\  
&& apk add --no-cache --no-progress --virtual BUILD_DEPS \  
build-base \  
ca-certificates \  
curl \  
libpcap-dev \  
linux-headers \  
lzo-dev \  
openssl-dev \  
zlib-dev \  
&& apk add --no-cache --no-progress \  
libpcap \  
libcrypto1.0 \  
lzo \  
zlib \  
\  
# Install timonier/dumb-entrypoint  
\  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/dumb-entrypoint/installer" |
INSTALL_DIRECTORY="/usr/sbin" sh -s -- install \  
&& curl --location "https://github.com/timonier/dumb-
entrypoint/raw/master/src/gosu/installer" | INSTALL_DIRECTORY="/usr/sbin" sh
-s -- install \  
\  
# Install tinc  
\  
&& export $(curl --location "https://github.com/timonier/version-
lister/raw/generated/_/tinc/${TINC_VERSION}" | xargs) \  
&& curl --location "https://www.tinc-
vpn.org/packages/tinc-${TINC_VERSION}.tar.gz" | tar --directory /tmp --extract
--gzip \  
&& sh -c "cd '/tmp/tinc-${TINC_VERSION}' && ./configure --enable-jumbograms
--enable-lzo --enable-tunemu --enable-zlib --localstatedir=/var --prefix=/usr
--sysconfdir=/etc" \  
&& make --directory "/tmp/tinc-${TINC_VERSION}" \  
&& make --directory "/tmp/tinc-${TINC_VERSION}" install \  
\  
# Clean  
\  
&& apk del --no-progress \  
BUILD_DEPS \  
&& rm -f -r \  
/tmp/*  
  
ENTRYPOINT [ "dumb-entrypoint" ]  

