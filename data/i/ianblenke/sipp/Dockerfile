FROM alpine  
MAINTAINER Ian Blenke <ian@blenke.com>  
  
ENV SIPP_VERSION 3.4.1  
  
RUN apk update && \  
apk add \--update bash curl tar git make build-base automake autoconf gettext
libcrypto1.0 libpcap libpcap-dev lksctp-tools lksctp-tools-dev ncurses-libs
ncurses-dev linux-headers libstdc++ openssl-dev libssl1.0 libgcc musl musl-dev
sed grep && \  
mkdir /build && \  
cd /build && \  
curl -sqL https://github.com/SIPp/sipp/archive/v${SIPP_VERSION}.tar.gz | tar
xvzf - --strip-components=1 && \  
sed -i '1i#define _GNU_SOURCE' src/prepare_pcap.c && \  
sed -e 's/const u_char/const unsigned char/g' \  
-e 's/u_long/unsigned long/g' \  
-e 's/u_char/unsigned char/g' \  
-i `grep -r -e 'u_long\|u_char' src/ | cut -d: -f1 | sort | uniq` && \  
./configure --with-pcap --with-sctp --with-openssl --with-rtpstream && \  
make install && \  
rm -fr /build && \  
apk del sed grep musl linux-headers libpcap-dev lksctp-tools-dev ncurses-dev
openssl-dev automake autoconf build-base make git && \  
rm -rf /var/cache/apk/*  
  
CMD sipp  

