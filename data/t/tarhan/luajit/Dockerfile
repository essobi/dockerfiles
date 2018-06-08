FROM alpine:3.4  
  
MAINTAINER Dmitriy Lekomtsev <lekomtsev@gmail.com>  
  
ENV LUA_JIT_MAJOR_VERSION 2.1  
ENV LUA_JIT_VERSION 2.1.0-beta2  
ENV LUAROCKS_VERSION 2.4.0  
# Installing luajit, luarocks  
# As for packages installing Penlight "batteries" and lrexlib-pcre  
  
ENV SRC_DIR /app/src  
  
RUN mkdir -p $SRC_DIR \  
# Installing runtime dependecies of luarocks, lrexlib-pcre  
&& apk --no-cache add \  
pcre \  
readline \  
curl \  
libgcc \  
unzip \  
libstdc++ \  
openssl \  
# Temporary installing build dependencies for openresty and luarocks  
&& apk --no-cache add --virtual build-dependencies \  
build-base \  
cmake \  
git \  
readline-dev \  
curl-dev \  
perl \  
pcre-dev \  
openssl-dev \  
&& cd $SRC_DIR \  
# Installing LuaJIT  
&& curl -LO http://luajit.org/download/LuaJIT-$LUA_JIT_VERSION.tar.gz \  
&& tar xf LuaJIT-$LUA_JIT_VERSION.tar.gz \  
&& cd LuaJIT-$LUA_JIT_VERSION \  
&& make \  
&& make install \  
&& cd /usr/local/bin \  
&& ln -sf luajit-$LUA_JIT_VERSION luajit \  
&& ln -sf luajit lua \  
&& cd $SRC_DIR \  
&& rm -Rf LuaJIT* \  
# Installing luarocks  
&& curl -LO
http://keplerproject.github.io/luarocks/releases/luarocks-$LUAROCKS_VERSION.tar.gz
\  
&& tar xf luarocks-$LUAROCKS_VERSION.tar.gz \  
&& cd luarocks-$LUAROCKS_VERSION \  
&& ./configure \  
\--lua-suffix=jit \  
\--with-lua=/usr/local \  
\--with-lua-include=/usr/local/include/luajit-$LUA_JIT_MAJOR_VERSION \  
\--with-downloader=curl \  
&& make build \  
&& make install \  
&& cd $SRC_DIR \  
&& rm -rf luarocks-$LUAROCKS_VERSION* \  
# Installing luasec as it commonly used by luarocks for packages on github  
&& luarocks install luasocket \  
&& luarocks install luasec \  
# Installing Penlight "batteries"  
&& luarocks install luafilesystem \  
&& luarocks install penlight \  
# Installing Lrexlib regex library with PCRE flavour  
&& luarocks install lrexlib-pcre \  
&& apk del build-dependencies  
  
WORKDIR /app/src  
  
ENTRYPOINT ["/usr/local/bin/lua"]  

