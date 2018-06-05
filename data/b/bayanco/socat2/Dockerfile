FROM alpine:3.4  
  
RUN \  
apk add --update build-base openssl openssl-dev && \  
mkdir src && cd src && \  
wget http://www.dest-unreach.org/socat/download/socat-2.0.0-b9.tar.gz && \  
tar xzvf socat-2.0.0-b9.tar.gz && \  
cd socat-2.0.0-b9 && \  
wget git.alpinelinux.org/cgit/aports/plain/main/socat/netdb-internal.patch &&
\  
patch -i netdb-internal.patch && \  
./configure && \  
make && \  
make install && \  
apk del build-base openssl-dev && \  
rm -rf /src /var/cache/apk  
  
CMD ["socat"]  

