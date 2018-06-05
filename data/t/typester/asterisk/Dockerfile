FROM ubuntu:16.04  
MAINTAINER Daisuke Murase <typester@gmail.com>  
  
ENV ASTERISK_VERSION 13-current  
ENV PJSIP_VERSION 2.5.5  
RUN apt-get update && \  
DEBIAN_FRONTEND=noninteractive apt-get install -y \  
build-essential pkg-config curl libncurses5-dev uuid-dev libjansson-dev
libxml2-dev libssl-dev libgsm1-dev libopus-dev libsqlite3-dev \  
libspeex-dev libspeexdsp-dev libresample1-dev libvorbis-dev libogg-dev
libsrtp0-dev && \  
apt-get purge -y --auto-remove && rm -rf /var/lib/apt/lists/*  
  
RUN mkdir /usr/src/pjsip && \  
cd /usr/src/pjsip && \  
curl -sL
http://www.pjsip.org/release/${PJSIP_VERSION}/pjproject-${PJSIP_VERSION}.tar.bz2
| tar --strip-components 1 -xvj && \  
./configure --prefix=/usr --enable-shared --disable-sound --disable-resample
--disable-video --disable-opencore-amr CFLAGS='-O2 -DNDEBUG' && \  
make dep && make && make install && \  
ldconfig && \  
rm -rf /usr/src/pjsip  
  
RUN mkdir -p /usr/src/asterisk && \  
cd /usr/src/asterisk && \  
curl -sL
http://downloads.asterisk.org/pub/telephony/asterisk/asterisk-${ASTERISK_VERSION}.tar.gz
| tar --strip-components 1 -xvz && \  
./configure && \  
make menuselect menuselect.makeopts && \  
for c in WAV ULAW ALAW GSM G729 G722 SLN16; do ./menuselect/menuselect
--enable CORE-SOUNDS-JA-${c} menuselect.makeopts; done && \  
make && make install && \  
rm -rf /usr/src/asterisk  
  

