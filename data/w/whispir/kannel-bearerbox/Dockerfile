FROM alpine:latest as builder  
ADD gateway-1.4.4.tar.gz /kannel-src  
RUN apk add --no-cache bash libxml2 pcre musl hiredis libxml2-dev openssl \  
pcre-dev build-base libtool musl-dev bison hiredis-dev openssl-dev  
RUN ln -sf /usr/include/poll.h /usr/include/sys/poll.h  
RUN ln -s /usr/include/unistd.h /usr/include/sys/unistd.h  
RUN ln -s /usr/share/libtool/build-aux/ltmain.sh /kannel-src/ltmain.sh  
WORKDIR /kannel-src/gateway-1.4.4  
RUN rm -f wmlscript/wsgram.y  
RUN ./configure --with-redis --enable-docks=no --enable-start-stop-daemon=no \  
\--without-sdb --without-oracle --without-sqlite2  
RUN make  
  
FROM alpine:latest  
WORKDIR /kannel/bin  
ADD bearerbox-start.sh .  
ADD kannel.template /kannel  
ADD smsc.template /kannel  
RUN apk add --no-cache bash libxml2 pcre musl hiredis gettext openssl && \  
mkdir /kannel/log && mkdir /kannel/etc && \  
chmod +x /kannel/bin/bearerbox-start.sh  
COPY \--from=builder /kannel-src/gateway-1.4.4/gw/bearerbox .  
EXPOSE 13000  
EXPOSE 13001  
ENTRYPOINT [ "bash", "/kannel/bin/bearerbox-start.sh" ]

