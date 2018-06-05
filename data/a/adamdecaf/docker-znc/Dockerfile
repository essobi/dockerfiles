FROM alpine:3.4  
ENV ZNC_VERSION=1.6.4  
ENV
ZNC_CHECKSUM="431097eb17860bfc980f3e68fdd75f98af4bdeecd793c84835c6cb11c3320d1c
znc-$ZNC_VERSION.tar.gz"  
WORKDIR /opt/znc/  
RUN apk update && \  
apk add znc znc-extra znc-modperl znc-modpython znc-modtcl ca-certificates &&
\  
apk add autoconf automake gettext-dev g++ make openssl-dev pkgconfig wget
zlib-dev && \  
wget http://znc.in/releases/znc-"$ZNC_VERSION".tar.gz && \  
echo "$ZNC_CHECKSUM" > /tmp/znc.sig && \  
cat /tmp/znc.sig && \  
sha256sum znc-"$ZNC_VERSION".tar.gz && \  
sha256sum -c /tmp/znc.sig && \  
tar -xzvf znc-"$ZNC_VERSION".tar.gz && \  
rm znc-"$ZNC_VERSION".tar.gz && \  
cd znc-"$ZNC_VERSION" && \  
./configure && make && make install && \  
apk del autoconf automake gettext-dev g++ make openssl-dev pkgconfig wget
zlib-dev  
  
ADD run.sh /opt/znc/run.sh  
ENTRYPOINT ["/opt/znc/run.sh"]  

