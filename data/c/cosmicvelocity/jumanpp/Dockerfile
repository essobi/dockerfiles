FROM alpine:3.6  
MAINTAINER Kouichi Machida <k-machida@aideo.co.jp>  
  
ENV JUMAN_VERSION=7.01 \  
JUMANPP_VERSION=1.02 \  
KNP_VERSION=4.17  
ENV
JUMAN_DOWNLOAD_URL="http://nlp.ist.i.kyoto-u.ac.jp/DLcounter/lime.cgi?down=http://nlp.ist.i.kyoto-u.ac.jp/nl-
resource/juman/juman-${JUMAN_VERSION}.tar.bz2&name=juman-${JUMAN_VERSION}.tar.bz2"
\  
JUMANPP_DOWNLOAD_URL="http://nlp.ist.i.kyoto-u.ac.jp/DLcounter/lime.cgi?down=http://lotus.kuee.kyoto-u.ac.jp/nl-
resource/jumanpp/jumanpp-${JUMANPP_VERSION}.tar.xz&name=jumanpp-${JUMANPP_VERSION}.tar.xz"
\  
KNP_DOWNLOAD_URL="http://nlp.ist.i.kyoto-u.ac.jp/DLcounter/lime.cgi?down=http://nlp.ist.i.kyoto-u.ac.jp/nl-
resource/knp/knp-${KNP_VERSION}.tar.bz2&name=knp-${KNP_VERSION}.tar.bz2"  
  
RUN apk add --update --no-cache --virtual .build-deps-jumanpp \  
boost-dev \  
g++ \  
make \  
zlib-dev \  
\  
&& apk add --no-cache \  
boost \  
curl \  
\  
&& curl -L -o /tmp/juman.tar.bz2 "${JUMAN_DOWNLOAD_URL}" \  
&& tar xjvf /tmp/juman.tar.bz2 -C /tmp \  
&& cd /tmp/juman-${JUMAN_VERSION} \  
&& ./configure --prefix=/usr/local/ \  
&& make \  
&& make install \  
\  
&& curl -L -o /tmp/jumanpp.tar.xz "${JUMANPP_DOWNLOAD_URL}" \  
&& tar xJvf /tmp/jumanpp.tar.xz -C /tmp \  
&& cd /tmp/jumanpp-${JUMANPP_VERSION} \  
&& ./configure --prefix=/usr/local/ \  
&& make \  
&& make install \  
\  
&& curl -L -o /tmp/knp.tar.bz2 "${KNP_DOWNLOAD_URL}" \  
&& tar xjvf /tmp/knp.tar.bz2 -C /tmp \  
&& cd /tmp/knp-${KNP_VERSION} \  
&& ./configure --prefix=/usr/local/ \  
&& sed -i -e "/^KNP_LIB/s/$/ -lzlib/" Makefile \  
&& make \  
&& make install \  
\  
&& apk del .build-deps-jumanpp \  
\  
&& rm -rf /tmp/* \  
&& rm -rf /var/cache/apk/*  

