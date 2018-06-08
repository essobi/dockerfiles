FROM alpine:3.3  
MAINTAINER Matthew Endsley <mendsley@gmail.com>  
  
RUN buildDeps='curl tar g++' \  
NACL_DOWNLOAD='http://hyperelliptic.org/nacl/nacl-20110221.tar.bz2' \  
NACL_DOWNLOAD_SHA1='6007a6aee249f5a534ec53fddfc364601fba9629' \  
set -x \  
&& apk add --update $buildDeps \  
&& curl -sSL $NACL_DOWNLOAD -o nacl.tar.bz2 \  
&& echo "$NACL_DOWNLOAD_SHA1 *nacl.tar.bz2" | sha1sum -c - \  
&& mkdir -p /usr/src/nacl \  
&& tar -xjf nacl.tar.bz2 -C /usr/src/nacl --strip-components=1 \  
&& rm nacl.tar.bz2 \  
&& cd /usr/src/nacl \  
&& ./do \  
&& cd build/$(hostname) \  
&& mkdir -p /usr/include/nacl/ \  
&& cp -avr include/amd64/* /usr/include/nacl/ \  
&& cp -av lib/amd64/*.a /usr/lib/ \  
&& cd / \  
&& rm -rf /usr/src/nacl \  
&& apk del --purge $buildDeps \  
&& rm -rf /var/cache/apk/* \  
;  

