#  
# ZNC + Alpine Linux  
# Includes znc-palaver, znc-playback, znc-clientbuffer plugins  
#  
  
FROM alpine:edge  
  
ENV PALAVER_URL https://github.com/Palaver/znc-palaver/archive/master.zip  
ENV PLAYBACK_URL https://github.com/jpnurmi/znc-playback/archive/master.zip  
ENV CLIENTBUFFER_URL https://github.com/jpnurmi/znc-
clientbuffer/archive/master.zip  
  
# Append if desired: znc-modperl znc-modpython znc-modtcl  
RUN apk --update add build-base openssl-dev wget unzip ca-certificates znc
znc-dev znc-extra && \  
chown znc:znc /var/lib/znc && \  
wget -O /tmp/palaver.zip $PALAVER_URL && \  
unzip /tmp/palaver.zip -d /tmp && \  
cd /tmp/znc-palaver-master && \  
make && \  
cp palaver.so /usr/lib/znc/ && \  
wget -O /tmp/playback.zip $PLAYBACK_URL && \  
unzip /tmp/playback.zip -d /tmp && \  
cd /tmp/znc-playback-master && \  
znc-buildmod playback.cpp && \  
cp playback.so /usr/lib/znc && \  
wget -O /tmp/clientbuffer.zip $CLIENTBUFFER_URL && \  
unzip /tmp/clientbuffer.zip -d /tmp && \  
cd /tmp/znc-clientbuffer-master && \  
znc-buildmod clientbuffer.cpp && \  
cp clientbuffer.so /usr/lib/znc && \  
rm -rf /tmp/* && \  
apk del build-base openssl-dev wget unzip znc-dev && \  
rm -rf /var/cache/apk/*  
  
USER znc  
VOLUME ["/var/lib/znc"]  
  
ENTRYPOINT ["znc", "--foreground", "--datadir=/var/lib/znc"]  

