FROM alpine:latest  
  
# Original version by <brainsam@yandex.ru>  
# Further changes by <Johann du Toit>  
MAINTAINER tomek@swingdev.io  
  
RUN apk --update add git build-base automake libtool m4 autoconf libevent-dev
openssl-dev c-ares-dev && \  
git clone https://github.com/pgbouncer/pgbouncer.git && \  
cd pgbouncer && \  
git submodule init && \  
git submodule update && \  
./autogen.sh && \  
./configure --prefix=/usr/local \--with-libevent=/usr/lib && \  
make && make install && \  
apk del git build-base automake autoconf libtool m4 && \  
rm -f /var/cache/apk/* \  
&& cd .. && rm -Rf pgbouncer  
  
ADD entrypoint.sh ./  
  
ENTRYPOINT ["./entrypoint.sh"]  

