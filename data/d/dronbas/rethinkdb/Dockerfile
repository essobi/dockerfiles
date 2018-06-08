# https://github.com/rethinkdb/rethinkdb-
dockerfiles/issues/32#issuecomment-297428635  
FROM alpine:3.6  
  
ENV RETHINKDB_VERSION 2.3.5  
  
RUN mkdir /tmp/build_rethinkdb && cd /tmp/build_rethinkdb \  
&& apk add \--no-cache curl \--virtual .fetch-deps \  
&& curl -sSLO
https://download.rethinkdb.com/dist/rethinkdb-$RETHINKDB_VERSION.tgz \  
&& tar xf rethinkdb-$RETHINKDB_VERSION.tgz \  
&& cd rethinkdb-$RETHINKDB_VERSION \  
&& curl -sSLO
https://git.alpinelinux.org/cgit/aports/plain/community/rethinkdb/libressl.patch?h=3.5-stable
\  
&& patch -p1 -i libressl.patch?h=3.5-stable \  
&& apk del .fetch-deps \  
&& apk add \--no-cache protobuf libressl libcurl boost libexecinfo \  
&& apk add \--no-cache bash python2 linux-headers bsd-compat-headers m4
paxmark protobuf-dev icu-dev libressl-dev curl-dev boost-dev libexecinfo-dev
\--virtual .build-deps \  
&& apk add \--no-cache g++ make \--virtual .build-deps2 \  
&& ./configure \--prefix=/usr \--sysconfdir=/etc \--localstatedir=/var
\--dynamic all \--with-system-malloc \  
&& export CXXFLAGS="-fno-delete-null-pointer-checks" && export
LDFLAGS="-lexecinfo" && make SYMBOLS=0 \  
&& make install-binaries \  
&& apk del .build-deps && apk del .build-deps2 \  
&& rm -rf /tmp/build_rethinkdb  
  
VOLUME ["/data"]  
  
WORKDIR /data  
  
CMD ["rethinkdb", "--bind", "all"]  
  
# process cluster webui  
EXPOSE 28015 29015 8080

