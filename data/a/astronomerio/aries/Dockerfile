FROM alpine:3.5  
MAINTAINER astronomer <aries@astronomer.io>  
  
ENV STRONGSWAN_VERSION=5.5.1 \  
GPG_KEY=DF42C170B34DBA77 \  
OPENFORTIVPN_VERSION=v1.3.0 \  
LOG_PATH=/usr/local/src/log  
  
# install persistent packages  
RUN apk add --no-cache \  
bash \  
bind-tools \  
openssl-dev \  
expect \  
ppp  
  
# install strongswan  
RUN apk --update upgrade \  
&& apk add ca-certificates wget \  
&& update-ca-certificates \  
&& apk add --no-cache --virtual .build-deps \  
gmp-dev \  
gnupg \  
g++ \  
gcc \  
libgcc \  
linux-headers \  
make \  
&& mkdir -p /usr/src/strongswan \  
&& cd /usr/src \  
&& wget
https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.bz2.sig \  
&& wget https://download.strongswan.org/strongswan-$STRONGSWAN_VERSION.tar.bz2
\  
&& export GNUPGHOME="$(mktemp -d)" \  
&& gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$GPG_KEY" \  
&& gpg --batch --verify strongswan-$STRONGSWAN_VERSION.tar.bz2.sig
strongswan-$STRONGSWAN_VERSION.tar.bz2 \  
&& tar xjvf strongswan-$STRONGSWAN_VERSION.tar.bz2 -C /usr/src/strongswan
--strip-components 1 \  
&& cd /usr/src/strongswan \  
&& ./configure --prefix=/usr --sysconfdir=/etc \  
\--enable-eap-radius \  
\--enable-eap-mschapv2 \  
\--enable-eap-identity \  
\--enable-eap-md5 \  
\--enable-eap-mschapv2 \  
\--enable-eap-tls \  
\--enable-eap-ttls \  
\--enable-eap-peap \  
\--enable-eap-tnc \  
\--enable-eap-dynamic \  
\--enable-xauth-eap \  
\--enable-openssl \  
&& make -j \  
&& make install \  
&& rm -rf /usr/src/strongswan* \  
&& apk del .build-deps  
  
# Install openfortivpn  
RUN apk --update upgrade \  
&& apk add ca-certificates wget \  
&& update-ca-certificates \  
&& apk add --no-cache --virtual .build-deps \  
automake \  
autoconf \  
g++ \  
gcc \  
make \  
&& mkdir -p /usr/src/openfortivpn \  
&& cd /usr/src/openfortivpn \  
&& wget
https://github.com/adrienverge/openfortivpn/archive/${OPENFORTIVPN_VERSION}.tar.gz
\  
&& tar xvf $OPENFORTIVPN_VERSION.tar.gz --strip-components 1 \  
&& cd /usr/src/openfortivpn \  
&& aclocal && autoconf && automake --add-missing \  
&& ./configure --prefix=/usr --sysconfdir=/etc \  
&& make \  
&& make install \  
&& apk del .build-deps  
  
# Make directory for logs  
RUN mkdir -p $LOG_PATH  
  
# COPY scripts  
COPY scripts /usr/local/bin/  

