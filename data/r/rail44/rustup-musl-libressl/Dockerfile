FROM rail44/rustup-musl:nightly  
RUN mkdir -p /opt/libressl-dev-musl  
RUN curl http://dl-3.alpinelinux.org/alpine/edge/main/x86_64/libressl-dev-$( \  
curl -sSL http://dl-3.alpinelinux.org/alpine/edge/main/x86_64/APKINDEX.tar.gz
| \  
tar -Oxz | \  
grep --text '^P:libressl-dev$' -A1 | \  
tail -n1 | \  
cut -d: -f2 \  
).apk | tar zxC /opt/libressl-dev-musl  
ENV OPENSSL_STATIC=1  
ENV OPENSSL_INCLUDE_DIR=/opt/libressl-dev-musl/usr/include  
ENV OPENSSL_LIB_DIR=/opt/libressl-dev-musl/usr/lib  

