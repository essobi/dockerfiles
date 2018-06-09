FROM iotsec/arm-alpine  
  
ENV SURICATA_RELEASE https://github.com/OISF/suricata/  
  
RUN apk --update add build-base \  
libtool \  
m4 \  
autoconf \  
automake \  
gettext \  
pcre \  
pcre-dev \  
libpcap-dev \  
libnet-dev \  
yaml-dev \  
zlib \  
zlib-dev \  
libcap-ng-dev \  
libcap-ng \  
libmagic \  
jansson-dev \  
libhtp-dev \  
libhtp \  
git \  
curl \  
openssl \  
ca-certificates \  
libnetfilter_queue \  
libnetfilter_queue-dev \  
iptables \  
hiredis-dev \  
libevent-dev &&\  
git clone $SURICATA_RELEASE /tmp/suricata/ && \  
cd /tmp/suricata/ && \  
./autogen.sh && \  
./configure --enable-pie \  
\--enable-non-bundled-htp \  
\--enable-nfqueue \  
\--enable-hiredis && \  
make && \  
make install-full && \  
rm -rf /tmp/* && \  
apk del build-base git && \  
rm -rf /var/cache/apk/*  
  
COPY ./ipflush.stop /etc/local.d/ipflush.stop  
  
RUN chmod +x /etc/local.d/ipflush.stop  
  
CMD suricata -q 0 -q 1 -q 2  

