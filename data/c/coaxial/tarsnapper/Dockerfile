FROM python:3.6-alpine  
LABEL "maintainer"="Coaxial, https://64b.it"  
  
ENV TARSNAP_VERSION 1.0.39  
ENV TARSNAP_SHA256
5613218b2a1060c730b6c4a14c2b34ce33898dd19b38fb9ea0858c5517e42082  
ENV TARSNAPPER_VERSION 0.4.0  
# Download, verify, compile, and install tarsnap  
RUN apk add --no-cache gcc libc-dev make openssl openssl-dev zlib-dev
e2fsprogs-dev &&\  
wget https://www.tarsnap.com/download/tarsnap-autoconf-$TARSNAP_VERSION.tgz
&&\  
hash=$(sha256sum tarsnap-autoconf-$TARSNAP_VERSION.tgz | cut -d ' ' -f 1) &&\  
if [ "$hash" !=
"5613218b2a1060c730b6c4a14c2b34ce33898dd19b38fb9ea0858c5517e42082" ]; then
echo "sha256 mismatch, tarsnap archive might not be authentic, aborting.";
exit 1; fi &&\  
tar -xzf tarsnap-autoconf-$TARSNAP_VERSION.tgz &&\  
cd tarsnap-autoconf-$TARSNAP_VERSION/ &&\  
./configure &&\  
make all install clean &&\  
cd .. &&\  
rm -rf tarsnap-autoconf-$TARSNAP_VERSION.tgz &&\  
rm -rf tarsnap-autoconf-$TARSNAP_VERSION &&\  
apk del gcc libc-dev make openssl openssl-dev zlib-dev e2fsprogs-dev  
  
# Install tarsnapper  
RUN pip install tarsnapper==$TARSNAPPER_VERSION &&\  
mkdir -p /etc/cron.d/tarsnapper  
  
VOLUME /backup  
  
ADD ./bootstrap.sh /bootstrap.sh  
ADD ./check-tarsnap-cache.sh /check-tarsnap-cache.sh  
ADD ./run-backup.sh /run-backup.sh  
  
CMD /bootstrap.sh  

