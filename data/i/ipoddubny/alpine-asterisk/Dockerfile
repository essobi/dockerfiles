FROM alpine:latest  
MAINTAINER Ivan Poddubny <ivan.poddubny@gmail.com>  
WORKDIR /root/  
  
COPY src ./src  
  
ENV ASTERISK_VERSION 15.3.0  
  
RUN apk update \  
&& apk add libtool libuuid jansson libxml2 sqlite-libs readline libcurl
libressl zlib libsrtp lua5.1-libs spandsp unbound-libs \  
&& apk add --virtual .build-deps gnupg build-base patch bsd-compat-headers
util-linux-dev ncurses-dev libresample \  
jansson-dev libxml2-dev sqlite-dev readline-dev curl-dev libressl-dev unbound-
dev \  
zlib-dev libsrtp-dev lua-dev spandsp-dev \  
&& export GNUPGHOME="$(mktemp -d)" \  
&& for key in \  
551F29104B2106080C6C2851073B0C1FC9B2E352 \  
21A91EB1F012252993E9BF4A368AB332B59975F3 \  
80CEBC345EC9FF529B4B7B808438CBA18D0CAA72 \  
639D932D5170532F8C200CCD9C59F000777DCC45 \  
57E769BC37906C091E7F641F6CB44E557BD982D8 \  
CDBEE4CC699E200EB4D46BB79E76E3A42341CE04 \  
; do \  
gpg --keyserver pgp.mit.edu --recv-keys "$key" || \  
gpg --keyserver keyserver.pgp.com --recv-keys "$key" || \  
gpg --keyserver ha.pool.sks-keyservers.net --recv-keys "$key" ; \  
done \  
&& wget
http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-${ASTERISK_VERSION}.tar.gz
\  
&& wget
http://downloads.asterisk.org/pub/telephony/asterisk/releases/asterisk-${ASTERISK_VERSION}.tar.gz.asc
\  
&& gpg --batch --verify asterisk-${ASTERISK_VERSION}.tar.gz.asc
asterisk-${ASTERISK_VERSION}.tar.gz \  
&& rm -rf "$GNUPGHOME" asterisk-${ASTERISK_VERSION}.tar.gz.asc \  
&& tar xzf asterisk-${ASTERISK_VERSION}.tar.gz \  
&& cd asterisk-${ASTERISK_VERSION} \  
&& sed -i -e 's/ASTSSL_LIBS:=$(OPENSSL_LIB)/ASTSSL_LIBS:=-Wl,--no-as-needed
$(OPENSSL_LIB) -Wl,--as-needed/g' main/Makefile \  
&& patch -p1 < ../src/musl-mutex-init.patch \  
&& cp ../src/9000-libressl.patch third-party/pjproject/patches/ \  
&& ./configure --with-pjproject-bundled \  
&& make menuselect.makeopts \  
&& ./menuselect/menuselect \  
\--disable BUILD_NATIVE \  
\--disable-category MENUSELECT_CORE_SOUNDS \  
\--disable-category MENUSELECT_MOH \  
\--disable-category MENUSELECT_EXTRA_SOUNDS \  
\--disable app_externalivr \  
\--disable app_adsiprog \  
\--disable app_alarmreceiver \  
\--disable app_getcpeid \  
\--disable app_minivm \  
\--disable app_morsecode \  
\--disable app_mp3 \  
\--disable app_nbscat \  
\--disable app_zapateller \  
\--disable chan_mgcp \  
\--disable chan_skinny \  
\--disable chan_unistim \  
\--disable codec_lpc10 \  
\--disable pbx_dundi \  
\--disable res_adsi \  
\--disable res_smdi \  
menuselect.makeopts \  
&& make -j$(getconf _NPROCESSORS_ONLN) ASTCFLAGS="-Os -fomit-frame-pointer"
ASTLDFLAGS="-Wl,--as-needed" \  
&& scanelf --recursive --nobanner --osabi --etype "ET_DYN,ET_EXEC" . \  
| while read type osabi filename ; do \  
[ "$osabi" != "STANDALONE" ] || continue ; \  
strip "${filename}" ; \  
done \  
&& make install \  
&& cd .. \  
&& apk del .build-deps \  
&& rm -rf ./asterisk* \  
&& rm -rf src \  
&& rm -rf /var/cache/apk/*  

