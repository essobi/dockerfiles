#  
# MonaServer Dockerfile  
  
FROM alpine  
  
MAINTAINER Thomas Jammet contact@monaserver.ovh  
  
ENV LUAJIT_VERSION 2.0.4  
ENV LUAJIT_DOWNLOAD_SHA256
620fa4eb12375021bef6e4f237cbd2dd5d49e56beb414bee052c746beef1807d  
ENV MONA_VERSION 1.2  
ENV MONA_DOWNLOAD_SHA256
fd176fc50b83629d13fa295c976096d943b64ce03b6b751c3dae22f05777cabf  
  
# install prerequisites  
RUN apk add \--no-cache libgcc \  
libstdc++ \  
openssl-dev \  
&& apk add \--no-cache \--virtual .build-deps \  
curl \  
make \  
g++ \  
  
# Build & install luajit  
&& mkdir -p /usr/src \  
&& cd /usr/src \  
&& curl -fSL -o luajit.tar.gz
http://luajit.org/download/LuaJIT-$LUAJIT_VERSION.tar.gz \  
&& echo "$LUAJIT_DOWNLOAD_SHA256 *luajit.tar.gz" | sha256sum -c \  
&& tar -xzf luajit.tar.gz \  
&& rm luajit.tar.gz \  
&& cd LuaJIT-$LUAJIT_VERSION \  
&& sed -i 's/#XCFLAGS+= -DLUAJIT_ENABLE_LUA52COMPAT/XCFLAGS+=
-DLUAJIT_ENABLE_LUA52COMPAT/g' src/Makefile \  
&& make \  
&& make install \  
# Correction of luajit-2.0.4 link name (TODO: delete it on next version)  
&& ln -s /usr/local/lib/libluajit-5.1.so.2.0.4
/usr/local/lib/libluajit-5.1.so.2 \  
&& cd ../ \  
&& rm -Rf LuaJIT-$LUAJIT_VERSION \  
  
# Build & install MonaServer  
&& curl -SL -o mona.tar.gz
https://github.com/MonaSolutions/MonaServer/archive/$MONA_VERSION.tar.gz \  
&& echo "$MONA_DOWNLOAD_SHA256 *mona.tar.gz" | sha256sum -c \  
&& tar -xzf mona.tar.gz \  
&& rm mona.tar.gz \  
&& cd MonaServer-$MONA_VERSION \  
# don't know why /usr/local/include/ is ignored by default  
&& cd MonaBase && make && cd ../MonaCore && make && cd ../MonaServer && make
INCLUDES="-I/usr/local/include/"\  
&& cp ../MonaBase/lib/libMonaBase.so ../MonaCore/lib/libMonaCore.so
/usr/local/lib \  
&& cp MonaServer /usr/local/bin \  
&& rm -Rf /usr/src/MonaServer-$MONA_VERSION \  
&& apk del .build-deps  
  
WORKDIR /usr/local/bin  
  
EXPOSE 80 1935 554  
  
# Set MonaServer as default executable  
CMD ["./MonaServer", "--log=7"]  

