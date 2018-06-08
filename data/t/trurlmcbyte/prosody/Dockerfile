FROM alpine:latest  
  
MAINTAINER Trurl McByte <trurl@mcbyte.net>  
  
ENV VERSION=0.9 \  
LUAVER=5.1  
# Install dependencies  
RUN apk add --no-cache \  
lua$LUAVER \  
lua-dbi-mysql \  
lua-dbi-postgresql \  
lua-dbi-sqlite \  
# lua-bitop \  
lua-bitlib \  
# lua-event \  
lua-evdev \  
lua-expat \  
lua-filesystem \  
lua-sec \  
lua-socket \  
curl \  
xz  
  
RUN apk add --no-cache --virtual .build-deps \  
gcc \  
libc-dev \  
make \  
autoconf \  
git \  
mercurial \  
patch \  
libidn-dev \  
libssl1.0 \  
openssl-dev \  
zlib-dev \  
libevent-dev \  
lua$LUAVER-dev \  
&& addgroup prosody \  
&& adduser -D \  
-h /var/lib/prosody \  
-s /sbin/nologin \  
-g "Prosody XMPP Server" \  
-G prosody \  
prosody \  
&& mkdir -p /usr/local/src \  
&& cd /usr/local/src \  
&& git clone https://github.com/brimworks/lua-zlib.git \  
&& cd lua-zlib \  
&& git checkout v0.2 \  
&& make linux \  
&& install -Dm755 zlib.so /usr/lib/lua/$LUAVER/zlib.so \  
&& cd /usr/local/src \  
&& git clone https://github.com/harningt/luaevent.git \  
&& cd luaevent \  
&& git checkout v0.4.3 \  
&& make \  
&& make install INSTALL_DIR_LUA=/usr/share/lua/$LUAVER
INSTALL_DIR_BIN=/usr/lib/lua/$LUAVER \  
&& cd /usr/local/src \  
&& curl -s http://bitop.luajit.org/download/LuaBitOp-1.0.2.tar.gz | tar -xz \  
&& cd LuaBitOp-1.0.2 \  
&& make \  
&& install -Dm755 bit.so /usr/lib/lua/$LUAVER/bit.so \  
&& cd /usr/local/src \  
&& hg clone https://hg.prosody.im/$VERSION prosody-$VERSION \  
# && curl -s https://prosody.im/downloads/source/prosody-$VERSION.tar.gz | tar
-xz \  
&& cd /usr/local/src/prosody-$VERSION \  
&& ./configure \  
\--prefix=/usr \  
\--sysconfdir=/etc/prosody \  
\--with-lua=/usr/bin \  
\--with-lua-lib=/usr/lib \  
\--with-lua-include=/usr/include \  
\--runwith=lua$LUAVER \  
\--no-example-certs \  
&& rm -f certs/Makefile \  
&& make \  
&& make install \  
&& install -d -o prosody -g prosody "$pkgdir/var/log/prosody" \  
&& install -d -o prosody -g prosody "$pkgdir/var/run/prosody" \  
&& install -d -m750 -o prosody -g prosody "$pkgdir/var/lib/prosody" \  
&& runDeps="$( \  
scanelf --needed --nobanner --recursive /usr/lib/prosody /usr/bin/prosody
/usr/lib/lua/$LUAVER/ \  
| awk '{ gsub(/,/, "\nso:", $2); print "so:" $2 }' \  
| sort -u \  
| xargs -r apk info --installed \  
| sort -u \  
)" \  
&& apk add --virtual .run-deps $runDeps \  
&& apk del .build-deps \  
&& rm -rf /usr/local/src/* \  
&& sed '1s/^/daemonize = false;\n/' /etc/prosody/prosody.cfg.lua >
/etc/prosody/prosody.cfg.lua.sample \  
&& sed -i 's/"prosody.log"/"\\*console"/' /etc/prosody/prosody.cfg.lua.sample
\  
&& sed -i 's/"prosody.err"/"\\*console"/' /etc/prosody/prosody.cfg.lua.sample  
  
COPY ./entrypoint.sh /entrypoint.sh  
COPY etc /etc/prosody  
  
RUN chmod 755 /entrypoint.sh && chown -R prosody /etc/prosody  
  
ENTRYPOINT ["/entrypoint.sh"]  
EXPOSE 80 443 5002 5222 5269 5347 5280 5281  
USER prosody  
VOLUME /var/lib/prosody  
CMD ["prosody"]  

